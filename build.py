#!/usr/bin/env python

import errno
import io
import os
import subprocess
import sys
from distutils import log, sysconfig
from distutils.ccompiler import new_compiler
from distutils.command.build_ext import build_ext
from distutils.core import Command, Distribution, Extension
from distutils.sysconfig import customize_compiler
from distutils.util import change_root

import pybind11

POGA_VERSION = "0.1.14a4"
YOGA_VERSION_REQUIRED = "1.19.0"


def get_command_class(name):
    # in case pip loads with setuptools this returns the extended commands
    return Distribution({}).get_command_class(name)


def _check_output(command):
    try:
        return subprocess.check_output(command)
    except OSError as e:
        if e.errno == errno.ENOENT:
            raise SystemExit("%r not found.\nCommand %r" % (command[0], command))
        raise SystemExit(e)
    except subprocess.CalledProcessError as e:
        raise SystemExit(e)


def pkg_config_version_check(pkg, version):
    pkg_config = os.environ.get("PKG_CONFIG", "pkg-config")
    command = [
        pkg_config,
        "--print-errors",
        "--exists",
        "%s >= %s" % (pkg, version),
    ]

    _check_output(command)


def pkg_config_parse(opt, pkg):
    pkg_config = os.environ.get("PKG_CONFIG", "pkg-config")
    command = [pkg_config, opt, pkg]
    ret = _check_output(command)
    output = ret.decode()
    opt = opt[-2:]
    return [x.lstrip(opt) for x in output.split()]


def filter_compiler_arguments(compiler, args):
    """Given a compiler instance and a list of compiler warning flags
    returns the list of supported flags.
    """

    if compiler.compiler_type == "msvc":
        # TODO
        return []

    extra = []

    def check_arguments(compiler, args):
        p = subprocess.Popen(
            [compiler.compiler[0]] + args + extra + ["-x", "c++", "-E", "-"],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        stdout, stderr = p.communicate(b"int i;\n")
        if p.returncode != 0:
            text = stderr.decode("ascii", "replace")
            return False, [a for a in args if a in text]
        else:
            return True, []

    def check_argument(compiler, arg):
        return check_arguments(compiler, [arg])[0]

    # clang doesn't error out for unknown options, force it to
    if check_argument(compiler, "-Werror=unknown-warning-option"):
        extra += ["-Werror=unknown-warning-option"]
    if check_argument(compiler, "-Werror=unused-command-line-argument"):
        extra += ["-Werror=unused-command-line-argument"]

    # first try to remove all arguments contained in the error message
    supported = list(args)
    while 1:
        ok, maybe_unknown = check_arguments(compiler, supported)
        if ok:
            return supported
        elif not maybe_unknown:
            break
        for unknown in maybe_unknown:
            if not check_argument(compiler, unknown):
                supported.remove(unknown)

    # hm, didn't work, try each argument one by one
    supported = []
    for arg in args:
        if check_argument(compiler, arg):
            supported.append(arg)
    return supported


def add_ext_cflags(ext, compiler):
    args = [
        "-Wall",
        "-Warray-bounds",
        "-Wcast-align",
        "-Wconversion",
        "-Wextra",
        "-Wformat=2",
        "-Wformat-nonliteral",
        "-Wformat-security",
        "-Wimplicit-function-declaration",
        "-Winit-self",
        "-Winline",
        "-Wmissing-format-attribute",
        "-Wmissing-noreturn",
        "-Wnested-externs",
        "-Wold-style-definition",
        "-Wpacked",
        "-Wpointer-arith",
        "-Wreturn-type",
        "-Wshadow",
        "-Wsign-compare",
        "-Wstrict-aliasing",
        "-Wundef",
        "-Wunused-but-set-variable",
        "-Wswitch-default",
    ]

    args += [
        "-Wno-missing-field-initializers",
        "-Wno-unused-parameter",
    ]

    # silence clang for unused gcc CFLAGS added by Debian
    args += [
        "-Wno-unused-command-line-argument",
    ]

    args += [
        "-fno-strict-aliasing",
        "-fvisibility=hidden",
        "-fno-omit-frame-pointer",
        "-fexceptions",
        "-ffunction-sections",
        "-fdata-sections",
        "-std=gnu++17",
    ]

    if sys.platform == "darwin":
        args += [
            "-mmacosx-version-min=10.9",
        ]

    ext.extra_compile_args += filter_compiler_arguments(compiler, args)


class install_pkgconfig(Command):
    description = "install .pc file"
    user_options = [
        ("pkgconfigdir=", None, "pkg-config file install directory"),
    ]

    def initialize_options(self):
        self.root = None
        self.install_base = None
        self.install_data = None
        self.pkgconfigdir = None
        self.compiler_type = None
        self.outfiles = []

    def finalize_options(self):
        self.set_undefined_options(
            "install_lib",
            ("install_base", "install_base"),
            ("install_data", "install_data"),
        )

        self.set_undefined_options(
            "install",
            ("root", "root"),
        )

        self.set_undefined_options(
            "build_ext",
            ("compiler_type", "compiler_type"),
        )

    def get_outputs(self):
        return self.outfiles

    def get_inputs(self):
        return []

    def run(self):
        cmd = self.distribution.get_command_obj("bdist_wheel", create=False)
        if cmd is not None:
            log.info("Skipping install_pkgconfig, not supported with bdist_wheel")
            return

        # same for bdist_egg
        cmd = self.distribution.get_command_obj("bdist_egg", create=False)
        if cmd is not None:
            log.info("Skipping install_pkgconfig, not supported with bdist_egg")
            return

        if self.compiler_type == "msvc":
            log.info("Skipping install_pkgconfig, not supported with MSVC")
            return

        if self.pkgconfigdir is None:
            python_lib = sysconfig.get_python_lib(True, True, self.install_data)
            pkgconfig_dir = os.path.join(os.path.dirname(python_lib), "pkgconfig")
        else:
            pkgconfig_dir = change_root(self.root, self.pkgconfigdir)
        self.mkpath(pkgconfig_dir)

        pcname = "poga.pc"
        target = os.path.join(pkgconfig_dir, pcname)

        log.info("Writing %s" % target)
        log.info("pkg-config prefix: %s" % self.install_base)
        with open(target, "wb") as h:
            h.write(
                (
                    """\
prefix=%(prefix)s
Name: poga
Description: Python %(py_version)d bindings for YogaLayout
Version: %(version)s
Requires: YogaLayout
Cflags: -I${prefix}/include/poga
Libs:
"""
                    % {"prefix": self.install_base, "version": POGA_VERSION, "py_version": sys.version_info[0]}
                ).encode("utf-8")
            )

        self.outfiles.append(target)


class install_poga_header(Command):
    description = "install poga header"
    user_options = []

    def initialize_options(self):
        self.install_data = None
        self.install_lib = None
        self.force = None
        self.outfiles = []

    def finalize_options(self):
        self.set_undefined_options(
            "install_lib",
            ("install_data", "install_data"),
            ("install_lib", "install_lib"),
        )

        self.set_undefined_options(
            "install",
            ("force", "force"),
        )

    def get_outputs(self):
        return self.outfiles

    def get_inputs(self):
        return [os.path.join("src/poga/capi", "poga.hpp")]

    def run(self):
        hname = "poga.hpp"
        source = self.get_inputs()[0]

        # for things using get_include()
        lib_hdir = os.path.join(self.install_lib, "poga", "include")
        self.mkpath(lib_hdir)
        lib_header_path = os.path.join(lib_hdir, hname)
        (out, _) = self.copy_file(source, lib_header_path)
        self.outfiles.append(out)

        cmd = self.distribution.get_command_obj("bdist_wheel", create=False)
        if cmd is not None:
            return
        cmd = self.distribution.get_command_obj("bdist_egg", create=False)
        if cmd is not None:
            return

        # for things using pkg-config
        data_hdir = os.path.join(self.install_data, "include", "poga")
        self.mkpath(data_hdir)
        header_path = os.path.join(data_hdir, hname)
        (out, _) = self.copy_file(source, header_path)
        self.outfiles.append(out)


def check_setuptools_for_dist():
    if "setuptools" not in sys.modules:
        raise Exception("setuptools not available")


du_sdist = get_command_class("sdist")


class sdist(du_sdist):
    def run(self):
        check_setuptools_for_dist()
        du_sdist.run(self)


du_install_lib = get_command_class("install_lib")


class install_lib(du_install_lib):
    def initialize_options(self):
        self.install_base = None
        self.install_lib = None
        self.install_data = None
        du_install_lib.initialize_options(self)

    def finalize_options(self):
        du_install_lib.finalize_options(self)
        self.set_undefined_options(
            "install",
            ("install_base", "install_base"),
            ("install_lib", "install_lib"),
            ("install_data", "install_data"),
        )

    def run(self):
        du_install_lib.run(self)
        # bdist_egg doesn't run install, so run our commands here instead
        self.run_command("install_pkgconfig")
        self.run_command("install_poga_header")


du_build_ext = get_command_class("build_ext")


class build_ext(du_build_ext):
    def initialize_options(self):
        du_build_ext.initialize_options(self)
        self.compiler_type = None

    def finalize_options(self):
        du_build_ext.finalize_options(self)

        self.compiler_type = new_compiler(compiler=self.compiler).compiler_type

    def run(self):
        ext = self.extensions[0]

        # If we are using MSVC, don't use pkg-config,
        # just assume that INCLUDE and LIB contain
        # the paths to the Cairo headers and libraries,
        # respectively.
        if self.compiler_type == "msvc":
            args = [
                "/std:c++17",
            ]
            ext.extra_compile_args += args
            # ext.libraries += ["yoga"]
        else:
            # ext.libraries += ["yoga"]
            # pkg_config_version_check('pybind11', YOGA_VERSION_REQUIRED)
            # ext.include_dirs += pkg_config_parse('--cflags-only-I', 'libyoga')
            # ext.library_dirs += pkg_config_parse('--libs-only-L', 'libyoga')
            # ext.libraries += pkg_config_parse('--libs-only-l', 'libyoga')
            compiler = new_compiler(compiler=self.compiler)
            customize_compiler(compiler)
            add_ext_cflags(ext, compiler)

        du_build_ext.run(self)


def build(setup_kwargs):
    poga_ext = Extension(
        name="poga.libpoga_capi",
        sources=[
            "src/poga/capi/poga_cmodule.cpp",
            "src/poga/capi/poga_manager.cpp",
            # Yoga src
            "src/poga/deps/yoga/event/event.cpp",
            "src/poga/deps/yoga/internal/experiments.cpp",
            "src/poga/deps/yoga/log.cpp",
            "src/poga/deps/yoga/Utils.cpp",
            "src/poga/deps/yoga/YGConfig.cpp",
            "src/poga/deps/yoga/YGEnums.cpp",
            "src/poga/deps/yoga/YGLayout.cpp",
            "src/poga/deps/yoga/YGNode.cpp",
            "src/poga/deps/yoga/YGNodePrint.cpp",
            "src/poga/deps/yoga/YGStyle.cpp",
            "src/poga/deps/yoga/YGValue.cpp",
            "src/poga/deps/yoga/Yoga.cpp",
        ],
        libraries=[],
        library_dirs=[],
        include_dirs=[
            "src/poga/deps",
            "src/poga/deps/yoga",
            pybind11.get_include(),
        ],
        define_macros=[
            ("POGA_VERSION_MAJOR", POGA_VERSION.split(".")[0]),
            ("POGA_VERSION_MINOR", POGA_VERSION.split(".")[1]),
            ("POGA_VERSION_MICRO", POGA_VERSION.split(".")[2]),
        ],
    )

    cmdclass = {
        "build_ext": build_ext,
        # "install_lib": install_lib,
        # "install_pkgconfig": install_pkgconfig,
        # "install_poga_header": install_poga_header,
        # # "test": test_cmd,
        # # "build_tests": build_tests,
        # "sdist": sdist,
    }

    setup_kwargs.update(
        {
            "ext_modules": [poga_ext],
            "cmdclass": cmdclass,
        }
    )

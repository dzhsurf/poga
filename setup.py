#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import re
import shutil
import sys
from distutils import log

import pybind11
from setuptools import Extension, find_packages, setup
from setuptools.command.build_ext import build_ext

POGA_VERSION = "0.1.17"

# obtain workdir
here = os.path.abspath(os.path.dirname(__file__))


class BuildExt(build_ext):
    c_opts = {
        "msvc": ["/EHsc", "/std:c++17"],
        "unix": ["-std=c++17"],
    }

    if sys.platform == "darwin":
        c_opts["unix"] += ["-stdlib=libc++", "-mmacosx-version-min=10.7"]

    def build_extensions(self):
        ct = self.compiler.compiler_type
        opts = self.c_opts.get(ct, [])
        for ext in self.extensions:
            ext.extra_compile_args = opts
        build_ext.build_extensions(self)

    def run(self):
        build_ext.run(self)
        self.copy_shared_libs_to_src()

    def copy_shared_libs_to_src(self):
        for ext in self.extensions:
            full_path = self.get_ext_fullpath(ext.name)
            target_dir = os.path.join(here, "src", "poga")
            if not os.path.exists(target_dir):
                os.makedirs(target_dir)
            target_path = os.path.join(target_dir, os.path.basename(full_path))
            log.info("Copying %s -> %s", full_path, target_path)
            shutil.copyfile(full_path, target_path)


ext_modules = [
    Extension(
        "poga.libpoga_capi",
        [
            os.path.join("src", "poga", "capi", "poga_cmodule.cpp"),
            os.path.join("src", "poga", "capi", "poga_manager.cpp"),
            # Yoga src
            os.path.join("src", "poga", "deps", "yoga", "event", "event.cpp"),
            os.path.join("src", "poga", "deps", "yoga", "internal", "experiments.cpp"),
            os.path.join("src", "poga", "deps", "yoga", "log.cpp"),
            os.path.join("src", "poga", "deps", "yoga", "Utils.cpp"),
            os.path.join("src", "poga", "deps", "yoga", "YGConfig.cpp"),
            os.path.join("src", "poga", "deps", "yoga", "YGEnums.cpp"),
            os.path.join("src", "poga", "deps", "yoga", "YGLayout.cpp"),
            os.path.join("src", "poga", "deps", "yoga", "YGNode.cpp"),
            os.path.join("src", "poga", "deps", "yoga", "YGNodePrint.cpp"),
            os.path.join("src", "poga", "deps", "yoga", "YGStyle.cpp"),
            os.path.join("src", "poga", "deps", "yoga", "YGValue.cpp"),
            os.path.join("src", "poga", "deps", "yoga", "Yoga.cpp"),
        ],
        define_macros=[
            ("POGA_VERSION_MAJOR", POGA_VERSION.split(".")[0]),
            ("POGA_VERSION_MINOR", POGA_VERSION.split(".")[1]),
            ("POGA_VERSION_MICRO", POGA_VERSION.split(".")[2]),
        ],
        include_dirs=[
            pybind11.get_include(False),
            pybind11.get_include(True),
            os.path.join(here, "src", "poga", "deps"),
            os.path.join(here, "src", "poga", "deps", "yoga"),
            os.path.join(here, "src", "poga", "deps", "yoga", "event"),
            os.path.join(here, "src", "poga", "deps", "yoga", "internal"),
            os.path.join(here, "src", "poga", "capi"),
        ],
        language="c++",
    ),
]

if __name__ == "__main__":
    if len(sys.argv) == 1:
        sys.argv.append("bdist_wheel")

    setup(
        name="poga",
        version=POGA_VERSION,
        package_dir={"": "src"},
        packages=find_packages(where="src"),
        ext_modules=ext_modules,
        install_requires=["pybind11>=2.2.0"],
        cmdclass={"build_ext": BuildExt},
        zip_safe=False,
    )

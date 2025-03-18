#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import re
import sys

import pybind11
from setuptools import Extension, find_packages, setup
from setuptools.command.build_ext import build_ext

POGA_VERSION = "0.1.14a4"

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
        package_dir={"": "src"},
        packages=find_packages(where="src"),
        ext_modules=ext_modules,
        install_requires=["pybind11>=2.2.0"],
        cmdclass={"build_ext": BuildExt},
        zip_safe=False,
    )

Poga Documentation
=================

[![Docs](https://img.shields.io/badge/docs-latest-informational)](https://dzhsurf.github.io/poga/)

Introduction
-----------------

Poga is a Python binding for YogaLayout.

It provides Python API for YogaLayout. And a high-level interface PogaLayout.

Install
-------

```shell
    # Python version requires >= 3.7
    pip install poga
```

Quickstart
----------

Using high-level interface PogaLayout

More details you can refer to the PGLayout of the pydui-gtk project below.

https://github.com/dzhsurf/pydui

```python
    from poga import PogaLayout

    def main():
        layout = PogaLayout()
        layout.flex_direction = YGFlexDirection.FlexStart
        # ...
        layout.apply_layout()
```

Using Binding CAPI directily

```python
    from poga.libpoga_capi import *

    def main():
        node = YGNodeNew()
        YGNodeSetNodeType(node, YGNodeType.Default)
        YGNodeFree(node)
```

Building
--------

Since there's a need for a cpp compiler to build the python extension module, you should install the build-essential tools before you build the package. 

* Windows: `VS16 - VS2019 Build Tools`

* MacOS: `XCode Command Line Tools`

* Linux (Ubuntu):  `build-essential`

```shell
# checkout the code and enter the diretory
conda env create -f conda-env.yaml # setup the py env. highly recommended.
conda activate poga
# or you can just install the dependencies by poetry. 
poetry install
# after finish setup the environment. go to install the package.
pip install -e . # install package
cd src && pip install -e . # enter the src dictory use the setuptools to build the libpoga_capi module
# now, all done. run the sample code 
python example/main.py
```


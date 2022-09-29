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

TODO: ...

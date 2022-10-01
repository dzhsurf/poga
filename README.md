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



## Benchmark

```shell
kernprof -l benchmark.py
python -m line_profiler benchmark.py.lprof
```

MacBook Pro (15-inch, 2016)

* Processor 2.7GHz Quad-core Intel Core i7
* Memory 16GB 2133 MHz LPDDR3

    Timer unit: 1e-06 s
    
    Total time: 0.000157 s
    File: benchmark.py
    Function: stack_with_flex at line 12
    
    Line #  Hits         Time  Per Hit   % Time  Line Contents
    ==============================================================
    12                                           @profile
    13                                           def stack_with_flex():
    14         1         28.0     28.0     17.8      root = YGNodeNew()
    15         1          8.0      8.0      5.1      YGNodeStyleSetWidth(root, 100)
    16         1          2.0      2.0      1.3      YGNodeStyleSetHeight(root, 100)
    17        11          8.0      0.7      5.1      for i in range(10):
    18        10         27.0      2.7     17.2          child = YGNodeNew()
    19        10         17.0      1.7     10.8          YGNodeStyleSetFlex(child, i)
    20        10         17.0      1.7     10.8          YGNodeInsertChild(root, child, 0)
    21
    22         1         50.0     50.0     31.8      YGNodeCalculateLayout(root, YGUndefined, YGUndefined, YGDirection.LTR)
    23                                               # TODO:
    24                                               # YGNodeFreeRecursive(root)
    
    Total time: 0.000201 s
    File: benchmark.py
    Function: align_stretch_in_undefined_axis at line 26
    
    Line #      Hits         Time  Per Hit   % Time  Line Contents
    ==============================================================
        26                                           @profile
        27                                           def align_stretch_in_undefined_axis():
        28         1          2.0      2.0      1.0      root = YGNodeNew()
        29        11          6.0      0.5      3.0      for i in range(10):
        30        10         19.0      1.9      9.5          child = YGNodeNew()
        31        10         13.0      1.3      6.5          YGNodeStyleSetHeight(child, 20)
        32        10         23.0      2.3     11.4          YGNodeSetMeasureFunc(child, measure_fn)
        33        10         15.0      1.5      7.5          YGNodeInsertChild(root, child, 0)
        34
        35         1        123.0    123.0     61.2      YGNodeCalculateLayout(root, YGUndefined, YGUndefined, YGDirection.LTR)
        36                                               # YGNodeFreeRecursive(root)
    
    Total time: 0.001938 s
    File: benchmark.py
    Function: nested_flex at line 38
    
    Line #      Hits         Time  Per Hit   % Time  Line Contents
    ==============================================================
        38                                           @profile
        39                                           def nested_flex():
        40         1          6.0      6.0      0.3      root = YGNodeNew()
        41        11         10.0      0.9      0.5      for i in range(10):
        42        10         21.0      2.1      1.1          child = YGNodeNew()
        43        10         12.0      1.2      0.6          YGNodeStyleSetFlex(child, 1)
        44        10         16.0      1.6      0.8          YGNodeInsertChild(root, child, 0)
        45
        46       110         67.0      0.6      3.5          for ii in range(10):
        47       100        216.0      2.2     11.1              grand_child = YGNodeNew()
        48       100        136.0      1.4      7.0              YGNodeSetMeasureFunc(grand_child, measure_fn);
        49       100        112.0      1.1      5.8              YGNodeStyleSetFlex(grand_child, 1);
        50       100        152.0      1.5      7.8              YGNodeInsertChild(child, grand_child, 0);
        51
        52         1       1190.0   1190.0     61.4      YGNodeCalculateLayout(root, YGUndefined, YGUndefined, YGDirection.LTR)
        53                                               # YGNodeFreeRecursive(root)
    
    Total time: 0.086841 s
    File: benchmark.py
    Function: huge_nested_layout at line 56
    
    Line #      Hits         Time  Per Hit   % Time  Line Contents
    ==============================================================
        56                                           @profile
        57                                           def huge_nested_layout():
        58         1          6.0      6.0      0.0      root = YGNodeNew()
        59        11          7.0      0.6      0.0      for i in range(10):
        60        10         16.0      1.6      0.0          child = YGNodeNew();
        61        10          9.0      0.9      0.0          YGNodeStyleSetFlexGrow(child, 1)
        62        10         10.0      1.0      0.0          YGNodeStyleSetWidth(child, 10)
        63        10         10.0      1.0      0.0          YGNodeStyleSetHeight(child, 10)
        64        10         13.0      1.3      0.0          YGNodeInsertChild(root, child, 0)
        65
        66       110         54.0      0.5      0.1          for ii in range(10):
        67       100        189.0      1.9      0.2              grand_child = YGNodeNew()
        68       100        106.0      1.1      0.1              YGNodeStyleSetFlexDirection(grand_child, YGFlexDirection.Row)
        69       100         90.0      0.9      0.1              YGNodeStyleSetFlexGrow(grand_child, 1)
        70       100         89.0      0.9      0.1              YGNodeStyleSetWidth(grand_child, 10)
        71       100         86.0      0.9      0.1              YGNodeStyleSetHeight(grand_child, 10)
        72       100        116.0      1.2      0.1              YGNodeInsertChild(child, grand_child, 0)
        73
        74      1100        539.0      0.5      0.6              for iii in range(10):
        75      1000       1640.0      1.6      1.9                  grand_grand_child = YGNodeNew()
        76      1000        922.0      0.9      1.1                  YGNodeStyleSetFlexGrow(grand_grand_child, 1)
        77      1000        906.0      0.9      1.0                  YGNodeStyleSetWidth(grand_grand_child, 10)
        78      1000        909.0      0.9      1.0                  YGNodeStyleSetHeight(grand_grand_child, 10)
        79      1000       1142.0      1.1      1.3                  YGNodeInsertChild(grand_child, grand_grand_child, 0)
        80
        81     11000       5428.0      0.5      6.3                  for iiii in range(10):
        82     10000      16694.0      1.7     19.2                      grand_grand_grand_child = YGNodeNew()
        83     10000      10450.0      1.0     12.0                      YGNodeStyleSetFlexDirection(grand_grand_grand_child, YGFlexDirection.Row);
        84     10000       9240.0      0.9     10.6                      YGNodeStyleSetFlexGrow(grand_grand_grand_child, 1);
        85     10000       9187.0      0.9     10.6                      YGNodeStyleSetWidth(grand_grand_grand_child, 10);
        86     10000       9251.0      0.9     10.7                      YGNodeStyleSetHeight(grand_grand_grand_child, 10);
        87     10000      11221.0      1.1     12.9                      YGNodeInsertChild(grand_grand_child, grand_grand_grand_child, 0);
        88
        89         1       8511.0   8511.0      9.8      YGNodeCalculateLayout(root, YGUndefined, YGUndefined, YGDirection.LTR)
        90                                               # YGNodeFreeRecursive(root)

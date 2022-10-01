Poga
====

 [![Docs](https://img.shields.io/badge/docs-latest-informational)](https://dzhsurf.github.io/poga/) 



Introduction
-----------------

Poga is a Python binding for YogaLayout.

It provides Python API for YogaLayout. And a high-level interface PogaLayout.

YogaLayout: https://yogalayout.com/



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



Benchmark
---------

```shell
kernprof -l benchmark.py
python -m line_profiler benchmark.py.lprof
```

MacBook Pro (15-inch, 2016)

* Processor 2.7GHz Quad-core Intel Core i7
* Memory 16GB 2133 MHz LPDDR3



```
Timer unit: 1e-06 s

Total time: 0.000124 s
File: benchmark.py
Function: stack_with_flex at line 12

Line #      Hits         Time  Per Hit   % Time  Line Contents
    12                                           @profile
    13                                           def stack_with_flex():
    14         1         20.0     20.0     16.1      root = YGNodeNew()
    15         1          9.0      9.0      7.3      YGNodeStyleSetWidth(root, 100)
    16         1          3.0      3.0      2.4      YGNodeStyleSetHeight(root, 100)
    17        11         10.0      0.9      8.1      for i in range(10):
    18        10         17.0      1.7     13.7          child = YGNodeNew()
    19        10         12.0      1.2      9.7          YGNodeStyleSetFlex(child, i)
    20        10         12.0      1.2      9.7          YGNodeInsertChild(root, child, 0)
    21
    22         1         32.0     32.0     25.8      YGNodeCalculateLayout(root, YGUndefined, YGUndefined, YGDirection.LTR)
    23         1          9.0      9.0      7.3      YGNodeFreeRecursive(root)

Total time: 0.000152 s
File: benchmark.py
Function: align_stretch_in_undefined_axis at line 25

Line #      Hits         Time  Per Hit   % Time  Line Contents
    25                                           @profile
    26                                           def align_stretch_in_undefined_axis():
    27         1          5.0      5.0      3.3      root = YGNodeNew()
    28        11          6.0      0.5      3.9      for i in range(10):
    29        10         14.0      1.4      9.2          child = YGNodeNew()
    30        10         10.0      1.0      6.6          YGNodeStyleSetHeight(child, 20)
    31        10         10.0      1.0      6.6          YGNodeSetMeasureFunc(child, measure_fn)
    32        10         11.0      1.1      7.2          YGNodeInsertChild(root, child, 0)
    33
    34         1         92.0     92.0     60.5      YGNodeCalculateLayout(root, YGUndefined, YGUndefined, YGDirection.LTR)
    35         1          4.0      4.0      2.6      YGNodeFreeRecursive(root)

Total time: 0.001446 s
File: benchmark.py
Function: nested_flex at line 37

Line #      Hits         Time  Per Hit   % Time  Line Contents
    37                                           @profile
    38                                           def nested_flex():
    39         1          2.0      2.0      0.1      root = YGNodeNew()
    40        11          5.0      0.5      0.3      for i in range(10):
    41        10         19.0      1.9      1.3          child = YGNodeNew()
    42        10          9.0      0.9      0.6          YGNodeStyleSetFlex(child, 1)
    43        10         11.0      1.1      0.8          YGNodeInsertChild(root, child, 0)
    44
    45       110         47.0      0.4      3.3          for ii in range(10):
    46       100        157.0      1.6     10.9              grand_child = YGNodeNew()
    47       100        102.0      1.0      7.1              YGNodeSetMeasureFunc(grand_child, measure_fn);
    48       100         90.0      0.9      6.2              YGNodeStyleSetFlex(grand_child, 1);
    49       100        104.0      1.0      7.2              YGNodeInsertChild(child, grand_child, 0);
    50
    51         1        886.0    886.0     61.3      YGNodeCalculateLayout(root, YGUndefined, YGUndefined, YGDirection.LTR)
    52         1         14.0     14.0      1.0      YGNodeFreeRecursive(root)

Total time: 0.090743 s
File: benchmark.py
Function: huge_nested_layout at line 55

Line #      Hits         Time  Per Hit   % Time  Line Contents
    55                                           @profile
    56                                           def huge_nested_layout():
    57         1          2.0      2.0      0.0      root = YGNodeNew()
    58        11          6.0      0.5      0.0      for i in range(10):
    59        10         18.0      1.8      0.0          child = YGNodeNew();
    60        10          9.0      0.9      0.0          YGNodeStyleSetFlexGrow(child, 1)
    61        10         10.0      1.0      0.0          YGNodeStyleSetWidth(child, 10)
    62        10         10.0      1.0      0.0          YGNodeStyleSetHeight(child, 10)
    63        10         14.0      1.4      0.0          YGNodeInsertChild(root, child, 0)
    64
    65       110         51.0      0.5      0.1          for ii in range(10):
    66       100        170.0      1.7      0.2              grand_child = YGNodeNew()
    67       100        110.0      1.1      0.1              YGNodeStyleSetFlexDirection(grand_child, YGFlexDirection.Row)
    68       100         95.0      0.9      0.1              YGNodeStyleSetFlexGrow(grand_child, 1)
    69       100         98.0      1.0      0.1              YGNodeStyleSetWidth(grand_child, 10)
    70       100         93.0      0.9      0.1              YGNodeStyleSetHeight(grand_child, 10)
    71       100        117.0      1.2      0.1              YGNodeInsertChild(child, grand_child, 0)
    72
    73      1100        549.0      0.5      0.6              for iii in range(10):
    74      1000       1734.0      1.7      1.9                  grand_grand_child = YGNodeNew()
    75      1000       1004.0      1.0      1.1                  YGNodeStyleSetFlexGrow(grand_grand_child, 1)
    76      1000        959.0      1.0      1.1                  YGNodeStyleSetWidth(grand_grand_child, 10)
    77      1000        932.0      0.9      1.0                  YGNodeStyleSetHeight(grand_grand_child, 10)
    78      1000       1142.0      1.1      1.3                  YGNodeInsertChild(grand_child, grand_grand_child, 0)
    79
    80     11000       5273.0      0.5      5.8                  for iiii in range(10):
    81     10000      17194.0      1.7     18.9                      grand_grand_grand_child = YGNodeNew()
    82     10000      10855.0      1.1     12.0                      YGNodeStyleSetFlexDirection(grand_grand_grand_child, YGFlexDirection.Row);
    83     10000       9482.0      0.9     10.4                      YGNodeStyleSetFlexGrow(grand_grand_grand_child, 1);
    84     10000       9676.0      1.0     10.7                      YGNodeStyleSetWidth(grand_grand_grand_child, 10);
    85     10000       9376.0      0.9     10.3                      YGNodeStyleSetHeight(grand_grand_grand_child, 10);
    86     10000      11454.0      1.1     12.6                      YGNodeInsertChild(grand_grand_child, grand_grand_grand_child, 0);
    87
    88         1       8632.0   8632.0      9.5      YGNodeCalculateLayout(root, YGUndefined, YGUndefined, YGDirection.LTR)
    89         1       1678.0   1678.0      1.8      YGNodeFreeRecursive(root)
```

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

Use high-level interface PogaLayout

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

Use Binding CAPI directily

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
pip install -e . 
# or you can just install the dependencies by poetry. 
poetry install
# now, all done. run the sample code 
python src/example/main.py
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

Total time: 0.000141 s
File: benchmark.py
Function: stack_with_flex at line 14

Line #      Hits         Time  Per Hit   % Time  Line Contents
    14                                           @profile
    15                                           def stack_with_flex():
    16         1         20.0     20.0     14.2      root = YGNodeNew()
    17         1         10.0     10.0      7.1      YGNodeStyleSetWidth(root, 100)
    18         1          3.0      3.0      2.1      YGNodeStyleSetHeight(root, 100)
    19        11         10.0      0.9      7.1      for i in range(10):
    20        10         23.0      2.3     16.3          child = YGNodeNew()
    21        10         12.0      1.2      8.5          YGNodeStyleSetFlex(child, i)
    22        10         16.0      1.6     11.3          YGNodeInsertChild(root, child, 0)
    23
    24         1         37.0     37.0     26.2      YGNodeCalculateLayout(root, YGUndefined, YGUndefined, YGDirection.LTR)
    25         1         10.0     10.0      7.1      YGNodeFreeRecursive(root)

Total time: 0.000169 s
File: benchmark.py
Function: align_stretch_in_undefined_axis at line 28

Line #      Hits         Time  Per Hit   % Time  Line Contents
    28                                           @profile
    29                                           def align_stretch_in_undefined_axis():
    30         1          2.0      2.0      1.2      root = YGNodeNew()
    31        11          6.0      0.5      3.6      for i in range(10):
    32        10         14.0      1.4      8.3          child = YGNodeNew()
    33        10         10.0      1.0      5.9          YGNodeStyleSetHeight(child, 20)
    34        10         12.0      1.2      7.1          YGNodeSetMeasureFunc(child, measure_fn)
    35        10         12.0      1.2      7.1          YGNodeInsertChild(root, child, 0)
    36
    37         1        110.0    110.0     65.1      YGNodeCalculateLayout(root, YGUndefined, YGUndefined, YGDirection.LTR)
    38         1          3.0      3.0      1.8      YGNodeFreeRecursive(root)

Total time: 0.001685 s
File: benchmark.py
Function: nested_flex at line 41

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
    41                                           @profile
    42                                           def nested_flex():
    43         1          2.0      2.0      0.1      root = YGNodeNew()
    44        11          6.0      0.5      0.4      for i in range(10):
    45        10         17.0      1.7      1.0          child = YGNodeNew()
    46        10         11.0      1.1      0.7          YGNodeStyleSetFlex(child, 1)
    47        10         14.0      1.4      0.8          YGNodeInsertChild(root, child, 0)
    48
    49       110         53.0      0.5      3.1          for ii in range(10):
    50       100        197.0      2.0     11.7              grand_child = YGNodeNew()
    51       100        111.0      1.1      6.6              YGNodeSetMeasureFunc(grand_child, measure_fn)
    52       100        109.0      1.1      6.5              YGNodeStyleSetFlex(grand_child, 1)
    53       100        121.0      1.2      7.2              YGNodeInsertChild(child, grand_child, 0)
    54
    55         1       1029.0   1029.0     61.1      YGNodeCalculateLayout(root, YGUndefined, YGUndefined, YGDirection.LTR)
    56         1         15.0     15.0      0.9      YGNodeFreeRecursive(root)

Total time: 0.093843 s
File: benchmark.py
Function: huge_nested_layout at line 59

Line #      Hits         Time  Per Hit   % Time  Line Contents
    59                                           @profile
    60                                           def huge_nested_layout():
    61         1          2.0      2.0      0.0      root = YGNodeNew()
    62        11          6.0      0.5      0.0      for i in range(10):
    63        10         15.0      1.5      0.0          child = YGNodeNew()
    64        10         11.0      1.1      0.0          YGNodeStyleSetFlexGrow(child, 1)
    65        10         11.0      1.1      0.0          YGNodeStyleSetWidth(child, 10)
    66        10         11.0      1.1      0.0          YGNodeStyleSetHeight(child, 10)
    67        10         13.0      1.3      0.0          YGNodeInsertChild(root, child, 0)
    68
    69       110         44.0      0.4      0.0          for ii in range(10):
    70       100        178.0      1.8      0.2              grand_child = YGNodeNew()
    71       100        115.0      1.1      0.1              YGNodeStyleSetFlexDirection(grand_child, YGFlexDirection.Row)
    72       100        101.0      1.0      0.1              YGNodeStyleSetFlexGrow(grand_child, 1)
    73       100         97.0      1.0      0.1              YGNodeStyleSetWidth(grand_child, 10)
    74       100         98.0      1.0      0.1              YGNodeStyleSetHeight(grand_child, 10)
    75       100        114.0      1.1      0.1              YGNodeInsertChild(child, grand_child, 0)
    76
    77      1100        561.0      0.5      0.6              for iii in range(10):
    78      1000       1782.0      1.8      1.9                  grand_grand_child = YGNodeNew()
    79      1000       1037.0      1.0      1.1                  YGNodeStyleSetFlexGrow(grand_grand_child, 1)
    80      1000        997.0      1.0      1.1                  YGNodeStyleSetWidth(grand_grand_child, 10)
    81      1000        959.0      1.0      1.0                  YGNodeStyleSetHeight(grand_grand_child, 10)
    82      1000       1177.0      1.2      1.3                  YGNodeInsertChild(grand_child, grand_grand_child, 0)
    83
    84     11000       5725.0      0.5      6.1                  for iiii in range(10):
    85     10000      17682.0      1.8     18.8                      grand_grand_grand_child = YGNodeNew()
    86     10000      11032.0      1.1     11.8                      YGNodeStyleSetFlexDirection(grand_grand_grand_child, YGFlexDirection.Row)
    87     10000      10126.0      1.0     10.8                      YGNodeStyleSetFlexGrow(grand_grand_grand_child, 1)
    88     10000      10035.0      1.0     10.7                      YGNodeStyleSetWidth(grand_grand_grand_child, 10)
    89     10000       9814.0      1.0     10.5                      YGNodeStyleSetHeight(grand_grand_grand_child, 10)
    90     10000      11796.0      1.2     12.6                      YGNodeInsertChild(grand_grand_child, grand_grand_grand_child, 0)
    91
    92         1       8696.0   8696.0      9.3      YGNodeCalculateLayout(root, YGUndefined, YGUndefined, YGDirection.LTR)
    93         1       1608.0   1608.0      1.7      YGNodeFreeRecursive(root)
```

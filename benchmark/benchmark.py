from poga import *
from poga.libpoga_capi import *


def measure_fn(
    node: YGNodeRef, width: float, width_mode: YGMeasureMode, height: float, height_mode: YGMeasureMode
) -> YGSize:
    return YGSize(
        10 if width_mode == YGMeasureMode.Undefined else width,
        10 if height_mode == YGMeasureMode.Undefined else height,
    )


@profile
def stack_with_flex():
    root = YGNodeNew()
    YGNodeStyleSetWidth(root, 100)
    YGNodeStyleSetHeight(root, 100)
    for i in range(10):
        child = YGNodeNew()
        YGNodeStyleSetFlex(child, i)
        YGNodeInsertChild(root, child, 0)

    YGNodeCalculateLayout(root, YGUndefined, YGUndefined, YGDirection.LTR)
    YGNodeFreeRecursive(root)


@profile
def align_stretch_in_undefined_axis():
    root = YGNodeNew()
    for i in range(10):
        child = YGNodeNew()
        YGNodeStyleSetHeight(child, 20)
        YGNodeSetMeasureFunc(child, measure_fn)
        YGNodeInsertChild(root, child, 0)

    YGNodeCalculateLayout(root, YGUndefined, YGUndefined, YGDirection.LTR)
    YGNodeFreeRecursive(root)


@profile
def nested_flex():
    root = YGNodeNew()
    for i in range(10):
        child = YGNodeNew()
        YGNodeStyleSetFlex(child, 1)
        YGNodeInsertChild(root, child, 0)

        for ii in range(10):
            grand_child = YGNodeNew()
            YGNodeSetMeasureFunc(grand_child, measure_fn)
            YGNodeStyleSetFlex(grand_child, 1)
            YGNodeInsertChild(child, grand_child, 0)

    YGNodeCalculateLayout(root, YGUndefined, YGUndefined, YGDirection.LTR)
    YGNodeFreeRecursive(root)


@profile
def huge_nested_layout():
    root = YGNodeNew()
    for i in range(10):
        child = YGNodeNew()
        YGNodeStyleSetFlexGrow(child, 1)
        YGNodeStyleSetWidth(child, 10)
        YGNodeStyleSetHeight(child, 10)
        YGNodeInsertChild(root, child, 0)

        for ii in range(10):
            grand_child = YGNodeNew()
            YGNodeStyleSetFlexDirection(grand_child, YGFlexDirection.Row)
            YGNodeStyleSetFlexGrow(grand_child, 1)
            YGNodeStyleSetWidth(grand_child, 10)
            YGNodeStyleSetHeight(grand_child, 10)
            YGNodeInsertChild(child, grand_child, 0)

            for iii in range(10):
                grand_grand_child = YGNodeNew()
                YGNodeStyleSetFlexGrow(grand_grand_child, 1)
                YGNodeStyleSetWidth(grand_grand_child, 10)
                YGNodeStyleSetHeight(grand_grand_child, 10)
                YGNodeInsertChild(grand_child, grand_grand_child, 0)

                for iiii in range(10):
                    grand_grand_grand_child = YGNodeNew()
                    YGNodeStyleSetFlexDirection(grand_grand_grand_child, YGFlexDirection.Row)
                    YGNodeStyleSetFlexGrow(grand_grand_grand_child, 1)
                    YGNodeStyleSetWidth(grand_grand_grand_child, 10)
                    YGNodeStyleSetHeight(grand_grand_grand_child, 10)
                    YGNodeInsertChild(grand_grand_child, grand_grand_grand_child, 0)

    YGNodeCalculateLayout(root, YGUndefined, YGUndefined, YGDirection.LTR)
    YGNodeFreeRecursive(root)


def main():
    stack_with_flex()
    align_stretch_in_undefined_axis()
    nested_flex()
    huge_nested_layout()


if __name__ == "__main__":
    main()

from enum import Enum
from typing import Any, BinaryIO, ByteString, Callable, List, Optional, Sequence, Text, Tuple, TypeVar, Union

def poga_version() -> str: ...
def poga_version_string() -> str: ...

YGUndefined: float

class YGNodeRef: ...
class YGConfigRef: ...

class YGSize:
    width: float
    height: float
    def __init__(self, width: float, height: float): ...

class YGMeasureMode(Enum):
    Undefined = 0
    Exactly = 1
    AtMost = 2

class YGNodeType(Enum):
    Default = 0
    Text = 1

class YGDirection(Enum):
    Inherit = 0
    LTR = 1
    RTL = 2

class YGFlexDirection(Enum):
    Column = 0
    ColumnReverse = 1
    Row = 2
    RowReverse = 3

class YGAlign(Enum):
    Auto = 0
    FlexStart = 1
    Center = 2
    FlexEnd = 3
    Stretch = 4
    Baseline = 5
    SpaceBetween = 6
    SpaceAround = 7

class YGPositionType(Enum):
    Static = 0
    Relative = 1
    Absolute = 2

class YGWrap(Enum):
    NoWrap = 0
    Wrap = 1
    WrapReverse = 2

class YGJustify(Enum):
    FlexStart = 0
    Center = 1
    FlexEnd = 2
    SpaceBetween = 3
    SpaceAround = 4
    SpaceEvenly = 5

class YGOverflow(Enum):
    Visible = 0
    Hidden = 1
    Scroll = 2

class YGDisplay(Enum):
    Flex = 0
    DisplayNone = 1

class YGEdge(Enum):
    Left = 0
    Top = 1
    Right = 2
    Bottom = 3
    Start = 4
    End = 5
    Horizontal = 6
    Vertical = 7
    All = 8

class YGUnit(Enum):
    Undefined = 0
    Point = 1
    Percent = 2
    Auto = 3

class YGValue:
    value: float
    unit: YGUnit
    def __init__(self, value: float, unit: YGUnit): ...

class YGLogLevel(Enum):
    Error = 0
    Warn = 1
    Info = 2
    Debug = 3
    Verbose = 4
    Fatal = 5

class YGExperimentalFeature(Enum):
    WebFlexBasis = 0

def YGNodeNew() -> YGNodeRef: ...
def YGNodeNewWithConfig(config: YGConfigRef) -> YGNodeRef: ...
def YGNodeClone(node: YGNodeRef) -> YGNodeRef: ...
def YGNodeFree(node: YGNodeRef): ...
def YGNodeFreeRecursive(node: YGNodeRef): ...
def YGNodeReset(node: YGNodeRef): ...
def YGNodeInsertChild(node: YGNodeRef, child: YGNodeRef, index: int): ...
def YGNodeSwapChild(node: YGNodeRef, child: YGNodeRef, index: int): ...
def YGNodeRemoveChild(node: YGNodeRef, child: YGNodeRef): ...
def YGNodeRemoveAllChildren(node: YGNodeRef): ...
def YGNodeGetChild(node: YGNodeRef, index: int) -> YGNodeRef: ...
def YGNodeGetOwner(node: YGNodeRef) -> YGNodeRef: ...
def YGNodeGetParent(node: YGNodeRef) -> YGNodeRef: ...
def YGNodeGetChildCount(node: YGNodeRef) -> int: ...
def YGNodeSetChildren(node: YGNodeRef, children: List[YGNodeRef]): ...
def YGNodeSetIsReferenceBaseline(node: YGNodeRef, is_reference_baseline: bool): ...
def YGNodeIsReferenceBaseline(node: YGNodeRef) -> bool: ...
def YGNodeCalculateLayout(
    node: YGNodeRef, available_width: float, available_height: float, owner_direction: YGDirection
) -> None: ...
def YGNodeMarkDirty(node: YGNodeRef): ...
def YGNodeMarkDirtyAndPropogateToDescendants(node: YGNodeRef): ...
def YGNodeCanUseCachedMeasurement(
    width_mode: YGMeasureMode,
    width: float,
    height_mode: YGMeasureMode,
    height: float,
    last_width_mode: YGMeasureMode,
    last_width: float,
    last_height_mode: YGMeasureMode,
    last_height: float,
    last_computed_width: float,
    last_computed_height: float,
    margin_row: float,
    margin_column: float,
    config: YGConfigRef,
): ...
def YGNodeCopyStyle(dst_node: YGNodeRef, src_node: YGNodeRef): ...
def YGNodeGetContext(node: YGNodeRef) -> Any: ...
def YGNodeSetContext(node: YGNodeRef, ctx: Any): ...
def YGNodeHasMeasureFunc(node: YGNodeRef) -> bool: ...
def YGNodeSetMeasureFunc(
    node: YGNodeRef, func: Callable[[YGNodeRef, float, YGMeasureMode, float, YGMeasureMode], YGSize]
): ...
def YGNodeHasBaselineFunc(node: YGNodeRef) -> bool: ...
def YGNodeSetBaselineFunc(node: YGNodeRef, func: Callable[[YGNodeRef, float, float], float]): ...
def YGNodeGetHasNewLayout(node: YGNodeRef) -> bool: ...
def YGNodeSetHasNewLayout(node: YGNodeRef, has_new_layout: bool): ...
def YGNodeGetNodeType(node: YGNodeRef) -> YGNodeType: ...
def YGNodeSetNodeType(node: YGNodeRef, type: YGNodeType): ...
def YGNodeIsDirty(node: YGNodeRef) -> bool: ...
def YGNodeLayoutGetDidUseLegacyFlag(node: YGNodeRef) -> bool: ...
def YGNodeStyleSetDirection(node: YGNodeRef, direction: YGDirection): ...
def YGNodeStyleGetDirection(node: YGNodeRef) -> YGDirection: ...
def YGNodeStyleSetFlexDirection(node: YGNodeRef, flex_direction: YGFlexDirection): ...
def YGNodeStyleGetFlexDirection(node: YGNodeRef) -> YGFlexDirection: ...
def YGNodeStyleSetJustifyContent(node: YGNodeRef, justify_content: YGJustify): ...
def YGNodeStyleGetJustifyContent(node: YGNodeRef) -> YGJustify: ...
def YGNodeStyleSetAlignContent(node: YGNodeRef, align_content: YGAlign): ...
def YGNodeStyleGetAlignContent(node: YGNodeRef) -> YGAlign: ...
def YGNodeStyleSetAlignItems(node: YGNodeRef, align_items: YGAlign): ...
def YGNodeStyleGetAlignItems(node: YGNodeRef) -> YGAlign: ...
def YGNodeStyleSetAlignSelf(node: YGNodeRef, align_self: YGAlign): ...
def YGNodeStyleGetAlignSelf(node: YGNodeRef) -> YGAlign: ...
def YGNodeStyleSetPositionType(node: YGNodeRef, position_type: YGPositionType): ...
def YGNodeStyleGetPositionType(node: YGNodeRef) -> YGPositionType: ...
def YGNodeStyleSetFlexWrap(node: YGNodeRef, flex_wrap: YGWrap): ...
def YGNodeStyleGetFlexWrap(node: YGNodeRef) -> YGWrap: ...
def YGNodeStyleSetOverflow(node: YGNodeRef, overflow: YGOverflow): ...
def YGNodeStyleGetOverflow(node: YGNodeRef) -> YGOverflow: ...
def YGNodeStyleSetDisplay(node: YGNodeRef, display: YGDisplay): ...
def YGNodeStyleGetDisplay(node: YGNodeRef) -> YGDisplay: ...
def YGNodeStyleSetFlex(node: YGNodeRef, flex: float): ...
def YGNodeStyleGetFlex(node: YGNodeRef) -> float: ...
def YGNodeStyleSetFlexGrow(node: YGNodeRef, flex_grow: float): ...
def YGNodeStyleGetFlexGrow(node: YGNodeRef) -> float: ...
def YGNodeStyleSetFlexShrink(node: YGNodeRef, flex_shrink: float): ...
def YGNodeStyleGetFlexShrink(node: YGNodeRef) -> float: ...
def YGNodeStyleSetFlexBasis(node: YGNodeRef, basis: float): ...
def YGNodeStyleSetFlexBasisPercent(node: YGNodeRef, flex_basis: float): ...
def YGNodeStyleSetFlexBasisAuto(node: YGNodeRef): ...
def YGNodeStyleGetFlexBasis(node: YGNodeRef) -> YGValue: ...
def YGNodeStyleSetPosition(node: YGNodeRef, edge: YGEdge, position: float): ...
def YGNodeStyleSetPositionPercent(node: YGNodeRef, edge: YGEdge, position: float): ...
def YGNodeStyleGetPosition(node: YGNodeRef, edge: YGEdge) -> YGValue: ...
def YGNodeStyleSetMargin(node: YGNodeRef, edge: YGEdge, margin: float): ...
def YGNodeStyleSetMarginPercent(node: YGNodeRef, edge: YGEdge, margin: float): ...
def YGNodeStyleSetMarginAuto(node: YGNodeRef, edge: YGEdge): ...
def YGNodeStyleGetMargin(node: YGNodeRef, edge: YGEdge) -> YGValue: ...
def YGNodeStyleSetPadding(node: YGNodeRef, edge: YGEdge, padding: float): ...
def YGNodeStyleSetPaddingPercent(node: YGNodeRef, edge: YGEdge, padding: float): ...
def YGNodeStyleGetPadding(node: YGNodeRef, edge: YGEdge) -> YGValue: ...
def YGNodeStyleSetBorder(node: YGNodeRef, edge: YGEdge, border: float): ...
def YGNodeStyleGetBorder(node: YGNodeRef, edge: YGEdge) -> float: ...
def YGNodeStyleSetWidth(node: YGNodeRef, width: float): ...
def YGNodeStyleSetWidthPercent(node: YGNodeRef, width: float): ...
def YGNodeStyleSetWidthAuto(node: YGNodeRef): ...
def YGNodeStyleGetWidth(node: YGNodeRef) -> YGValue: ...
def YGNodeStyleSetHeight(node: YGNodeRef, height: float): ...
def YGNodeStyleSetHeightPercent(node: YGNodeRef, height: float): ...
def YGNodeStyleSetHeightAuto(node: YGNodeRef): ...
def YGNodeStyleGetHeight(node: YGNodeRef) -> YGValue: ...
def YGNodeStyleSetMinWidth(node: YGNodeRef, min_width: float): ...
def YGNodeStyleSetMinWidthPercent(node: YGNodeRef, min_width: float): ...
def YGNodeStyleGetMinWidth(node: YGNodeRef) -> YGValue: ...
def YGNodeStyleSetMinHeight(node: YGNodeRef, min_height: float): ...
def YGNodeStyleSetMinHeightPercent(node: YGNodeRef, min_height: float): ...
def YGNodeStyleGetMinHeight(node: YGNodeRef) -> YGValue: ...
def YGNodeStyleSetMaxWidth(node: YGNodeRef, max_width: float): ...
def YGNodeStyleSetMaxWidthPercent(node: YGNodeRef, max_width: float): ...
def YGNodeStyleGetMaxWidth(node: YGNodeRef) -> YGValue: ...
def YGNodeStyleSetMaxHeight(node: YGNodeRef, max_height: float): ...
def YGNodeStyleSetMaxHeightPercent(node: YGNodeRef, max_height: float): ...
def YGNodeStyleGetMaxHeight(node: YGNodeRef) -> YGValue: ...
def YGNodeStyleSetAspectRatio(node: YGNodeRef, aspect_ratio: float): ...
def YGNodeStyleGetAspectRatio(node: YGNodeRef) -> float: ...
def YGNodeLayoutGetLeft(node: YGNodeRef) -> float: ...
def YGNodeLayoutGetTop(node: YGNodeRef) -> float: ...
def YGNodeLayoutGetRight(node: YGNodeRef) -> float: ...
def YGNodeLayoutGetBottom(node: YGNodeRef) -> float: ...
def YGNodeLayoutGetWidth(node: YGNodeRef) -> float: ...
def YGNodeLayoutGetHeight(node: YGNodeRef) -> float: ...
def YGNodeLayoutGetDirection(node: YGNodeRef) -> YGDirection: ...
def YGNodeLayoutGetHadOverflow(node: YGNodeRef) -> bool: ...
def YGNodeLayoutGetDidLegacyStretchFlagAffectLayout(node: YGNodeRef) -> bool: ...
def YGNodeLayoutGetMargin(node: YGNodeRef, edge: YGEdge) -> float: ...
def YGNodeLayoutGetBorder(node: YGNodeRef, edge: YGEdge) -> float: ...
def YGNodeLayoutGetPadding(node: YGNodeRef, edge: YGEdge) -> float: ...
def YGConfigSetLogger(config: YGConfigRef, func: Callable[[YGConfigRef, YGNodeRef, YGLogLevel, str, Any], int]): ...
def YGConfigSetPrintTreeFlag(config: YGConfigRef, enabled: bool): ...
def YGConfigSetPointScaleFactor(config: YGConfigRef, pixels_in_point: float): ...
def YGConfigSetShouldDiffLayoutWithoutLegacyStretchBehaviour(config: YGConfigRef, should_diff_layout: bool): ...
def YGConfigSetUseLegacyStretchBehaviour(config: YGConfigRef, use_legacy_stretch_behaviour: bool): ...
def YGConfigNew() -> YGConfigRef: ...
def YGConfigFree(config: YGConfigRef): ...
def YGConfigCopy(dest: YGConfigRef, src: YGConfigRef): ...
def YGConfigGetInstanceCount() -> int: ...
def YGConfigSetExperimentalFeatureEnabled(config: YGConfigRef, feature: YGExperimentalFeature, enabled: bool): ...
def YGConfigSetUseWebDefaults(config: YGConfigRef, enabled: bool): ...
def YGConfigGetUseWebDefaults(config: YGConfigRef) -> bool: ...
def YGFloatIsUndefined(value: float) -> bool: ...
def YGRoundValueToPixelGrid(value: float, point_scale_factor: float, force_ceil: bool, force_floor: bool) -> float: ...
def YGNodeIsSame(node1: YGNodeRef, node2: YGNodeRef) -> bool: ...

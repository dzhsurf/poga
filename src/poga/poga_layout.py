import sys
import weakref
from enum import Enum
from math import isnan, nan
from typing import Any, Dict, Iterable, List, Tuple
from weakref import ReferenceType

from .libpoga_capi import *
from .poga_view import PogaView


class YGDimensionFlexibility(Enum):
    FlexibleWidth = 1 << 0
    FlexibleHeight = 1 << 1


class PogaLayout:
    """PogaLayout"""

    global __global_config
    __global_config = None

    __node: YGNodeRef = None
    __enabled: bool = True
    __is_included_in_layout: bool = True
    if sys.version_info >= (3, 9):
        # Python 3.9+ specific definitions and imports
        __view: ReferenceType[PogaView] = None
    else:
        __view: Any = None

    @staticmethod
    def release_global_config():
        global __global_config
        if PogaLayout.__global_config is not None:
            YGConfigFree(PogaLayout.__global_config)
            PogaLayout.__global_config = None

    @staticmethod
    def get_global_config() -> YGConfigRef:
        global __global_config
        if __global_config is None:
            __global_config = YGConfigNew()
            YGConfigSetExperimentalFeatureEnabled(__global_config, YGExperimentalFeature.WebFlexBasis, True)
            scale: float = 2.0  # TODO: get screen scale
            YGConfigSetPointScaleFactor(__global_config, scale)
        return __global_config

    def __init__(self, view: PogaView):
        self.__node = YGNodeNewWithConfig(PogaLayout.get_global_config())
        self.__enabled = True
        self.__is_included_in_layout = True
        self.__view = weakref.ref(view)
        YGNodeSetContext(self.__node, self.__view)
        # initial default value
        self.direction = YGDirection.LTR
        self.flex_direction = YGFlexDirection.Row
        self.align_content = YGAlign.FlexStart
        self.align_items = YGAlign.FlexStart
        self.align_self = YGAlign.Auto
        self.flex_wrap = YGWrap.Wrap
        self.justify_content = YGJustify.FlexStart
        # self.aspect_ratio

    def __del__(self):
        YGNodeSetContext(self.__node, None)
        YGNodeFree(self.__node)

    @property
    def is_included_in_layout(self) -> bool:
        return self.__is_included_in_layout

    @is_included_in_layout.setter
    def is_included_in_layout(self, is_included_in_layout: bool):
        self.__is_included_in_layout = is_included_in_layout

    @property
    def is_enabled(self) -> bool:
        return self.__enabled

    @is_enabled.setter
    def is_enabled(self, enabled: bool):
        self.__enabled = enabled

    @property
    def direction(self) -> YGDirection:
        return YGNodeStyleGetDirection(self.__node)

    @direction.setter
    def direction(self, direction: YGDirection):
        YGNodeStyleSetDirection(self.__node, direction)

    @property
    def flex_direction(self) -> YGFlexDirection:
        return YGNodeStyleGetFlexDirection(self.__node)

    @flex_direction.setter
    def flex_direction(self, flex_direction: YGFlexDirection):
        YGNodeStyleSetFlexDirection(self.__node, flex_direction)

    @property
    def justify_content(self) -> YGJustify:
        return YGNodeStyleGetJustifyContent(self.__node)

    @justify_content.setter
    def justify_content(self, justify_content: YGJustify):
        YGNodeStyleSetJustifyContent(self.__node, justify_content)

    @property
    def align_content(self) -> YGAlign:
        return YGNodeStyleGetAlignContent(self.__node)

    @align_content.setter
    def align_content(self, align_content: YGAlign):
        YGNodeStyleSetAlignContent(self.__node, align_content)

    @property
    def align_items(self) -> YGAlign:
        return YGNodeStyleGetAlignItems(self.__node)

    @align_items.setter
    def align_items(self, align_items: YGAlign):
        YGNodeStyleSetAlignItems(self.__node, align_items)

    @property
    def align_self(self) -> YGAlign:
        return YGNodeStyleGetAlignSelf(self.__node)

    @align_self.setter
    def align_self(self, align_self: YGAlign):
        YGNodeStyleSetAlignSelf(self.__node, align_self)

    @property
    def position(self) -> YGPositionType:
        return YGNodeStyleGetPositionType(self.__node)

    @position.setter
    def position(self, position: YGPositionType):
        YGNodeStyleSetPositionType(self.__node, position)

    @property
    def flex_wrap(self) -> YGWrap:
        return YGNodeStyleGetFlexWrap(self.__node)

    @flex_wrap.setter
    def flex_wrap(self, flex_wrap: YGWrap):
        YGNodeStyleSetFlexWrap(self.__node, flex_wrap)

    @property
    def overflow(self) -> YGOverflow:
        return YGNodeStyleGetOverflow(self.__node)

    @overflow.setter
    def overflow(self, overflow: YGOverflow):
        YGNodeStyleSetOverflow(self.__node, overflow)

    @property
    def display(self) -> YGDisplay:
        return YGNodeStyleGetDisplay(self.__node)

    @display.setter
    def display(self, display: YGDisplay):
        YGNodeStyleSetDisplay(self.__node, display)

    @property
    def flex(self) -> float:
        return YGNodeStyleGetFlex(self.__node)

    @flex.setter
    def flex(self, flex: float):
        YGNodeStyleSetFlex(self.__node, flex)

    @property
    def flex_grow(self) -> float:
        return YGNodeStyleGetFlexGrow(self.__node)

    @flex_grow.setter
    def flex_grow(self, flex_grow: float):
        YGNodeStyleSetFlexGrow(self.__node, flex_grow)

    @property
    def flex_shrink(self) -> float:
        return YGNodeStyleGetFlexShrink(self.__node)

    @flex_shrink.setter
    def flex_shrink(self, flex_shrink: float):
        YGNodeStyleSetFlexShrink(self.__node, flex_shrink)

    @property
    def flex_basis(self) -> YGValue:
        return YGNodeStyleGetFlexBasis(self.__node)

    @flex_basis.setter
    def flex_basis(self, flex_basis: YGValue):
        if flex_basis.unit == YGUnit.Point:
            YGNodeStyleSetFlexBasis(self.__node, flex_basis.value)
        elif flex_basis.unit == YGUnit.Percent:
            YGNodeStyleSetFlexBasisPercent(self.__node, flex_basis.value)
        elif flex_basis.unit == YGUnit.Auto:
            YGNodeStyleSetFlexBasisAuto(self.__node, flex_basis.value)

    def __get_position_by_edge__(self, edge: YGEdge) -> YGValue:
        return YGNodeStyleGetPosition(self.__node, edge)

    def __set_position_by_value__(self, edge: YGEdge, value: YGValue):
        if (value.unit == YGUnit.Point) or (value.unit == YGUnit.Undefined):
            YGNodeStyleSetPosition(self.__node, edge, value.value)
        elif value.unit == YGUnit.Percent:
            YGNodeStyleSetPositionPercent(self.__node, edge, value.value)

    @property
    def left(self) -> YGValue:
        return self.__get_position_by_edge__(YGEdge.Left)

    @left.setter
    def left(self, left: YGValue):
        self.__set_position_by_value__(YGEdge.Left, left)

    @property
    def top(self) -> YGValue:
        return self.__get_position_by_edge__(YGEdge.Top)

    @top.setter
    def top(self, top: YGValue):
        self.__set_position_by_edge__(YGEdge.Top, top)

    @property
    def right(self) -> YGValue:
        return self.__get_position_by_edge__(YGEdge.Right)

    @right.setter
    def right(self, right: YGValue):
        self.__set_position_by_edge__(YGEdge.Right, right)

    @property
    def bottom(self) -> YGValue:
        return self.__get_position_by_edge__(YGEdge.Bottom)

    @bottom.setter
    def bottom(self, bottom: YGValue):
        self.__set_position_by_edge__(YGEdge.Bottom, bottom)

    @property
    def start(self) -> YGValue:
        return self.__get_position_by_edge__(YGEdge.Start)

    @start.setter
    def start(self, start: YGValue):
        self.__set_position_by_edge__(YGEdge.Start, start)

    @property
    def end(self) -> YGValue:
        return self.__get_position_by_edge__(YGEdge.End)

    @end.setter
    def end(self, end: YGValue):
        self.__set_position_by_edge__(YGEdge.End, end)

    def __get_margin_by_edge__(self, edge: YGEdge) -> YGValue:
        return YGNodeStyleGetMargin(self.__node, edge)

    def __set_margin_by_edge__(self, edge: YGEdge, value: YGValue):
        if (value.unit == YGUnit.Undefined) or (value.unit == YGUnit.Point):
            YGNodeStyleSetMargin(self.__node, edge, value)
        elif value.unit == YGUnit.Percent:
            YGNodeStyleSetMarginPercent(self.__node, edge, value)
        elif value.unit == YGUnit.Auto:
            YGNodeStyleSetMarginAuto(self.__node, edge, value)

    @property
    def margin_left(self) -> YGValue:
        return self.__get_margin_by_edge__(YGEdge.Left)

    @margin_left.setter
    def margin_left(self, margin_left: YGValue):
        self.__set_margin_by_edge__(YGEdge.Left, margin_left)

    @property
    def margin_top(self) -> YGValue:
        return self.__get_margin_by_edge__(YGEdge.Top)

    @margin_top.setter
    def margin_top(self, margin_top: YGValue):
        self.__set_margin_by_edge__(YGEdge.Top, margin_top)

    @property
    def margin_right(self) -> YGValue:
        return self.__get_margin_by_edge__(YGEdge.Right)

    @margin_right.setter
    def margin_right(self, margin_right: YGValue):
        self.__set_margin_by_edge__(YGEdge.Right, margin_right)

    @property
    def margin_bottom(self) -> YGValue:
        return self.__get_margin_by_edge__(YGEdge.Bottom)

    @margin_bottom.setter
    def margin_bottom(self, margin_bottom: YGValue):
        self.__set_margin_by_edge__(YGEdge.Bottom, margin_bottom)

    @property
    def margin_start(self) -> YGValue:
        return self.__get_margin_by_edge__(YGEdge.Start)

    @margin_start.setter
    def margin_start(self, margin_start: YGValue):
        self.__set_margin_by_edge__(YGEdge.Start, margin_start)

    @property
    def margin_end(self) -> YGValue:
        return self.__get_margin_by_edge__(YGEdge.End)

    @margin_end.setter
    def margin_end(self, margin_end: YGValue):
        self.__get_margin_by_edge__(YGEdge.End, margin_end)

    @property
    def margin_horizontal(self) -> YGValue:
        return self.__get_margin_by_edge__(YGEdge.Horizontal)

    @margin_horizontal.setter
    def margin_horizontal(self, margin_horizontal: YGValue):
        self.__set_margin_by_edge__(YGEdge.Horizontal, margin_horizontal)

    @property
    def margin_vertical(self) -> YGValue:
        return self.__get_margin_by_edge__(YGEdge.Vertical)

    @margin_vertical.setter
    def margin_vertical(self, margin_vertical: YGValue):
        self.__set_margin_by_edge__(YGEdge.Vertical, margin_vertical)

    @property
    def margin(self) -> YGValue:
        return self.__get_margin_by_edge__(YGEdge.All)

    @margin.setter
    def margin(self, margin: YGValue):
        self.__set_margin_by_edge__(YGEdge.All, margin)

    def __get_padding_by_edge__(self, edge: YGEdge) -> YGValue:
        return YGNodeStyleGetMargin(self.__node, edge)

    def __set_padding_by_edge__(self, edge: YGEdge, value: YGValue):
        if (value.unit == YGUnit.Undefined) or (value.unit == YGUnit.Point):
            YGNodeStyleSetPadding(self.__node, edge, value)
        elif value.unit == YGUnit.Percent:
            YGNodeStyleSetPaddingPercent(self.__node, edge, value)

    @property
    def padding_left(self) -> YGValue:
        return self.__get_padding_by_edge__(YGEdge.Left)

    @padding_left.setter
    def padding_left(self, padding_left: YGValue):
        self.__set_padding_by_edge__(YGEdge.Left, padding_left)

    @property
    def padding_top(self) -> YGValue:
        return self.__get_padding_by_edge__(YGEdge.Left)

    @padding_top.setter
    def padding_top(self, padding_top: YGValue):
        self.__set_padding_by_edge__(YGEdge.Left, padding_top)

    @property
    def padding_right(self) -> YGValue:
        return self.__get_padding_by_edge__(YGEdge.Right)

    @padding_right.setter
    def padding_right(self, padding_right: YGValue):
        self.__set_padding_by_edge__()

    @property
    def padding_bottom(self) -> YGValue:
        return self.__get_padding_by_edge__(YGEdge.Bottom)

    @padding_bottom.setter
    def padding_bottom(self, padding_bottom: YGValue):
        self.__set_padding_by_edge__(YGEdge.Bottom, padding_bottom)

    @property
    def padding_start(self) -> YGValue:
        return self.__get_padding_by_edge__(YGEdge.Start)

    @padding_start.setter
    def padding_start(self, padding_start: YGValue):
        self.__set_padding_by_edge__(YGEdge.Start, padding_start)

    @property
    def padding_end(self) -> YGValue:
        return self.__get_padding_by_edge__(YGEdge.End)

    @padding_end.setter
    def padding_end(self, padding_end: YGValue):
        self.__set_padding_by_edge__(YGEdge.End, padding_end)

    @property
    def padding_horizontal(self) -> YGValue:
        return self.__get_padding_by_edge__(YGEdge.Horizontal)

    @padding_horizontal.setter
    def padding_horizontal(self, padding_horizontal: YGValue):
        self.__set_padding_by_edge__(YGEdge.Horizontal, padding_horizontal)

    @property
    def padding_vertical(self) -> YGValue:
        return self.__get_padding_by_edge__(YGEdge.Vertical)

    @padding_vertical.setter
    def padding_vertical(self, padding_vertical: YGValue):
        self.__set_padding_by_edge__(YGEdge.Vertical, padding_vertical)

    @property
    def padding(self) -> YGValue:
        return self.__get_padding_by_edge__(YGEdge.All)

    @padding.setter
    def padding(self, padding: YGValue):
        self.__set_padding_by_edge__(YGEdge.All, padding)

    def __get_border_by_edge__(self, edge: YGEdge) -> YGValue:
        return YGNodeStyleGetBorder(self.__node, edge)

    def __set_border_by_edge__(self, edge: YGEdge, value: float):
        YGNodeStyleSetBorder(self.__node, edge, value)

    @property
    def border_left_width(self) -> float:
        return self.__get_border_by_edge__(YGEdge.Left)

    @border_left_width.setter
    def border_left_width(self, border_left_width: float):
        self.__set_border_by_edge__(YGEdge.Left, border_left_width)

    @property
    def border_top_width(self) -> float:
        return self.__get_border_by_edge__(YGEdge.Top)

    @border_top_width.setter
    def border_top_width(self, border_top_width: float):
        self.__set_border_by_edge__(YGEdge.Top, border_top_width)

    @property
    def border_right_width(self) -> float:
        return self.__get_border_by_edge__(YGEdge.Right)

    @border_right_width.setter
    def border_right_width(self, border_right_width: float):
        self.__set_border_by_edge__(YGEdge.Right, border_right_width)

    @property
    def border_bottom_width(self) -> float:
        return self.__get_border_by_edge__(YGEdge.Bottom)

    @border_bottom_width.setter
    def border_bottom_width(self, border_bottom_width: float):
        self.__set_border_by_edge__(YGEdge.Bottom, border_bottom_width)

    @property
    def border_start_width(self) -> float:
        return self.__get_border_by_edge__(YGEdge.Start)

    @border_start_width.setter
    def border_start_width(self, border_start_width: float):
        self.__get_border_by_edge__(YGEdge.Start, border_start_width)

    @property
    def border_end_width(self) -> float:
        return self.__get_border_by_edge__(YGEdge.End)

    @border_end_width.setter
    def border_end_width(self, border_end_width: float):
        self.__set_border_by_edge__(YGEdge.End, border_end_width)

    @property
    def border_width(self) -> float:
        return self.__get_border_by_edge__(YGEdge.All)

    @border_width.setter
    def border_width(self, border_width: float):
        self.__set_border_by_edge__(YGEdge.All, border_width)

    @property
    def width(self) -> YGValue:
        return YGNodeStyleGetWidth(self.__node)

    @width.setter
    def width(self, width: YGValue):
        if width.unit == YGUnit.Point or width.unit == YGUnit.Undefined:
            YGNodeStyleSetWidth(self.__node, width.value)
        elif width.unit == YGUnit.Percent:
            YGNodeStyleSetWidthPercent(self.__node, width.value)
        elif width.unit == YGUnit.Auto:
            YGNodeStyleSetWidthAuto(self.__node)

    @property
    def height(self) -> YGValue:
        return YGNodeStyleGetHeight(self.__node)

    @height.setter
    def height(self, height: YGValue):
        if height.unit == YGUnit.Point or height.unit == YGUnit.Undefined:
            YGNodeStyleSetHeight(self.__node, height.value)
        elif height.unit == YGUnit.Percent:
            YGNodeStyleSetHeightPercent(self.__node, height.value)
        elif height.unit == YGUnit.Auto:
            YGNodeStyleSetHeightAuto(self.__node)

    @property
    def min_width(self) -> YGValue:
        return YGNodeStyleGetMinWidth(self.__node)

    @min_width.setter
    def min_width(self, min_width: YGValue):
        if min_width.unit == YGUnit.Point or min_width.unit == YGUnit.Undefined:
            YGNodeStyleSetMinWidth(self.__node, min_width.value)
        elif min_width.unit == YGUnit.Percent:
            YGNodeStyleSetMinWidthPercent(self.__node, min_width.value)

    @property
    def min_height(self) -> YGValue:
        return YGNodeStyleGetMinHeight(self.__node)

    @min_height.setter
    def min_height(self, min_height: YGValue):
        if min_height.unit == YGUnit.Point or min_height.unit == YGUnit.Undefined:
            YGNodeStyleSetMinHeight(self.__node, min_height.value)
        elif min_height.unit == YGUnit.Percent:
            YGNodeStyleSetMinHeightPercent(self.__node, min_height.value)

    @property
    def max_width(self) -> YGValue:
        return YGNodeStyleGetMaxWidth(self.__node)

    @max_width.setter
    def max_width(self, max_width: YGValue):
        if max_width.unit == YGUnit.Point or max_width.unit == YGUnit.Undefined:
            YGNodeStyleSetMinWidth(self.__node, max_width.value)
        elif max_width.unit == YGUnit.Percent:
            YGNodeStyleSetMinWidthPercent(self.__node, max_width.value)

    @property
    def max_height(self) -> YGValue:
        return YGNodeStyleGetMaxHeight(self.__node)

    @max_height.setter
    def max_height(self, max_height: YGValue):
        if max_height.unit == YGUnit.Point or max_height.unit == YGUnit.Undefined:
            YGNodeStyleSetMaxWidth(self.__node, max_height.value)
        elif max_height.unit == YGUnit.Percent:
            YGNodeStyleSetMaxWidthPercent(self.__node, max_height.value)

    @property
    def aspect_ratio(self) -> float:
        return YGNodeStyleGetAspectRatio(self.__node)

    @aspect_ratio.setter
    def aspect_ratio(self, aspect_ratio: float):
        YGNodeStyleSetAspectRatio(self.__node, aspect_ratio)

    @property
    def resolved_direction(self) -> YGDirection:
        return YGNodeLayoutGetDirection(self.__node)

    def apply_layout(self):
        self.apply_layout_preserving_origin(False)

    def apply_layout_preserving_origin(self, preserver_origin: bool):
        view = self.__view()
        if view is None:
            return

        bounds_size = view.bounds_size()
        self.calculate_layout_with_size(bounds_size)
        PogaLayout.__apply_layout_to_view_hierarchy__(view, preserver_origin)

    def apply_layout_preserving_origin_with_dimension_flexibility(
        self, preserver_origin: bool, dimension_flexibility: bool
    ):
        view = self.__view()
        if view is None:
            return

        bounds_size = view.bounds_size()
        if dimension_flexibility and YGDimensionFlexibility.FlexibleWidth:
            bounds_size = (YGUndefined, bounds_size[1])
        if dimension_flexibility and YGDimensionFlexibility.FlexibleHeight:
            bounds_size = (bounds_size[0], YGUndefined)
        self.calculate_layout_with_size(bounds_size)
        PogaLayout.__apply_layout_to_view_hierarchy__(view, preserver_origin)

    @property
    def intrinsic_size(self) -> Tuple[float, float]:
        constrained_size = [YGUndefined, YGUndefined]
        return self.calculate_layout_with_size(constrained_size)

    def calculate_layout_with_size(self, size: Tuple[float, float]) -> Tuple[float, float]:
        view = self.__view()
        if view is None:
            return (0.0, 0.0)

        PogaLayout.__attach_nodes_from_view_hierachy__(view)

        YGNodeCalculateLayout(self.__node, size[0], size[1], YGNodeStyleGetDirection(self.__node))
        return (YGNodeLayoutGetWidth(self.__node), YGNodeLayoutGetHeight(self.__node))

    @property
    def number_of_children(self) -> int:
        return YGNodeGetChildCount(self.__node)

    @property
    def is_leaf(self) -> bool:
        view = self.__view()
        if view is None:
            return True

        if self.is_enabled:
            for subview in view.subviews():
                poga_layout = subview.poga_layout()
                if poga_layout is None:
                    continue
                if poga_layout.is_enabled and poga_layout.is_included_in_layout:
                    return False

        return True

    @property
    def is_dirty(self) -> bool:
        return YGNodeIsDirty(self.__node)

    def mark_dirty(self):
        if self.is_dirty or not self.is_leaf:
            return
        if not YGNodeHasMeasureFunc(self.__node):
            YGNodeSetMeasureFunc(self.__node, PogaLayout.__measure_view__)

        YGNodeMarkDirty(self.__node)

    @staticmethod
    def __sanitize_measurement__(constrained_size: float, measured_size: float, measure_mode: YGMeasureMode):
        result: float = 0.0
        if measure_mode == YGMeasureMode.Exactly:
            result = constrained_size
        elif measure_mode == YGMeasureMode.AtMost:
            result = min(constrained_size, measured_size)
        else:
            result = measured_size
        return result

    @staticmethod
    def __measure_view__(
        node: YGNodeRef, width: float, width_mode: YGMeasureMode, height: float, height_mode: YGMeasureMode
    ) -> YGSize:
        constrained_width = sys.float_info.max if width_mode == YGMeasureMode.Undefined else width
        constrained_height = sys.float_info.max if height_mode == YGMeasureMode.Undefined else height

        weakref_view: ReferenceType[PogaView] = YGNodeGetContext(node)
        if weakref_view is None:
            return (0.0, 0.0)
        view = weakref_view()
        if view is None:
            return (0.0, 0.0)

        # size_that_fits = (0.0, 0.0)
        # if view.subviews_count() > 0:
        size_that_fits = view.size_that_fits(constrained_width, constrained_height)

        return YGSize(
            PogaLayout.__sanitize_measurement__(constrained_width, size_that_fits[0], width_mode),
            PogaLayout.__sanitize_measurement__(constrained_height, size_that_fits[1], height_mode),
        )

    @staticmethod
    def __round_pixel_value__(value: float) -> float:
        if isnan(value):
            return value
        scale = 2.0  # TODO
        return round(value * scale) / scale

    @staticmethod
    def __apply_layout_to_view_hierarchy__(view: PogaView, preserve_origin: bool):
        poga_layout = view.poga_layout()
        if poga_layout is None:
            return
        if not poga_layout.is_included_in_layout:
            return

        node = poga_layout.__node
        top_left = (
            YGNodeLayoutGetLeft(node),
            YGNodeLayoutGetTop(node),
        )
        bottom_right = (
            top_left[0] + YGNodeLayoutGetWidth(node),
            top_left[1] + YGNodeLayoutGetHeight(node),
        )

        origin = view.frame_origin() if preserve_origin else (0.0, 0.0)
        view.set_frame_origin(
            PogaLayout.__round_pixel_value__(top_left[0] + origin[0]),
            PogaLayout.__round_pixel_value__(top_left[1] + origin[1]),
        )
        view.set_frame_size(
            PogaLayout.__round_pixel_value__(bottom_right[0]) - PogaLayout.__round_pixel_value__(top_left[0]),
            PogaLayout.__round_pixel_value__(bottom_right[1]) - PogaLayout.__round_pixel_value__(top_left[1]),
        )

        if not poga_layout.is_leaf:
            for subview in view.subviews():
                PogaLayout.__apply_layout_to_view_hierarchy__(subview, False)

    @staticmethod
    def __has_exact_same_children__(node: YGNodeRef, subviews: List[PogaView]) -> bool:
        if YGNodeGetChildCount(node) != len(subviews):
            return False

        for i in range(len(subviews)):
            node1 = YGNodeGetChild(node, i)
            node2 = subviews[i].poga_layout().__node
            if not YGNodeIsSame(node1, node2):
                return False

        return True

    @staticmethod
    def __attach_nodes_from_view_hierachy__(view: PogaView):
        poga_layout = view.poga_layout()
        if poga_layout is None:
            return
        node = poga_layout.__node
        if poga_layout.is_leaf:
            YGNodeRemoveAllChildren(node)
            YGNodeSetMeasureFunc(node, PogaLayout.__measure_view__)
        else:
            YGNodeSetMeasureFunc(node, None)
            subviews_to_include = list[PogaView]()
            for subview in view.subviews():
                sub_poga = subview.poga_layout()
                if sub_poga is None:
                    continue
                if sub_poga.is_enabled and sub_poga.is_included_in_layout:
                    subviews_to_include.append(subview)
            if not PogaLayout.__has_exact_same_children__(node, subviews_to_include):
                YGNodeRemoveAllChildren(node)
                for i in range(len(subviews_to_include)):
                    child = subviews_to_include[i].poga_layout().__node
                    YGNodeInsertChild(node, child, i)

            for subview in subviews_to_include:
                PogaLayout.__attach_nodes_from_view_hierachy__(subview)

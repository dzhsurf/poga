import sys
from typing import Any, Dict, List, Tuple

from .libpoga_capi import *


class PogaLayout:
    __node: YGNodeRef = None
    __enabled: bool = True
    __direction: YGDirection = YGDirection.Inherit
    __flex_direction: YGDirection = YGDirection.Inherit
    __justify_content: YGJustify = YGJustify.FlexStart
    __align_content: YGAlign = YGAlign.Auto
    __align_items: YGAlign = YGAlign.Auto
    __align_self: YGAlign = YGAlign.Auto
    __position: YGPositionType = YGPositionType.Static
    __flex_wrap: YGWrap = YGWrap.NoWrap
    __overflow: YGOverflow = YGOverflow.Hidden
    __display: YGDisplay = YGDisplay.Flex
    __flex: float = 0.0
    __flex_grow: float = 0.0
    __flex_shrink: float = 0.0
    __flex_basis: float = 0.0
    __left: YGValue = None
    __top: YGValue = None
    __right: YGValue = None
    __bottom: YGValue = None
    __start: YGValue = None
    __end: YGValue = None

    __margin_left: YGValue = None
    __margin_top: YGValue = None
    __margin_right: YGValue = None
    __margin_bottom: YGValue = None
    __margin_start: YGValue = None
    __margin_end: YGValue = None
    __margin_horizontal: YGValue = None
    __margin_vertical: YGValue = None
    __margin: YGValue = None

    __padding_left: YGValue = None
    __padding_top: YGValue = None
    __padding_right: YGValue = None
    __padding_bottom: YGValue = None
    __padding_start: YGValue = None
    __padding_end: YGValue = None
    __padding_horizontal: YGValue = None
    __padding_vertical: YGValue = None
    __padding: YGValue = None

    __border_left_width: float = 0.0
    __border_top_width: float = 0.0
    __border_right_width: float = 0.0
    __border_bottom_width: float = 0.0
    __border_start_width: float = 0.0
    __border_end_width: float = 0.0
    __border_width: float = 0.0

    __width: YGValue = None
    __height: YGValue = None
    __min_width: YGValue = None
    __min_height: YGValue = None
    __max_width: YGValue = None
    __max_height: YGValue = None

    __aspect_ratio: float = 0.0

    def __init__(self):
        self.__node = YGNodeNew()

    def __del__(self):
        YGNodeFree(self.__node)

    @property
    def is_included_in_layout(self) -> bool:
        pass

    @is_included_in_layout.setter
    def is_included_in_layout(self, is_included_in_layout: bool):
        pass

    @property
    def is_enabled(self) -> bool:
        return self.__enabled

    @is_enabled.setter
    def is_enabled(self, enabled: bool):
        self.__enabled = enabled

    @property
    def direction(self) -> YGDirection:
        return self.__direction

    @direction.setter
    def direction(self, direction: YGDirection):
        self.__direction = direction

    @property
    def flex_direction(self) -> YGFlexDirection:
        return self.__flex_direction

    @flex_direction.setter
    def flex_direction(self, flex_direction: YGFlexDirection):
        self.__flex_direction = flex_direction

    @property
    def justify_content(self) -> YGJustify:
        return self.__justify_content

    @justify_content.setter
    def justify_content(self, justify_content: YGJustify):
        self.__justify_content = justify_content

    @property
    def align_content(self) -> YGAlign:
        return self.__align_content

    @align_content.setter
    def align_content(self, align_content: YGAlign):
        self.__align_content = align_content

    @property
    def align_items(self) -> YGAlign:
        return self.__align_items

    @align_items.setter
    def align_items(self, align_items: YGAlign):
        self.__align_items = align_items

    @property
    def align_self(self) -> YGAlign:
        return self.__align_self

    @align_self.setter
    def align_self(self, align_self: YGAlign):
        self.__align_self = align_self

    @property
    def position(self) -> YGPositionType:
        return self.__position

    @position.setter
    def position(self, position: YGPositionType):
        self.__position = position

    @property
    def flex_wrap(self) -> YGWrap:
        return self.__flex_wrap

    @flex_wrap.setter
    def flex_wrap(self, flex_wrap: YGWrap):
        self.__flex_wrap = flex_wrap

    @property
    def overflow(self) -> YGOverflow:
        return self.__overflow

    @overflow.setter
    def overflow(self, overflow: YGOverflow):
        self.__overflow = overflow

    @property
    def display(self) -> YGDisplay:
        return self.__display

    @display.setter
    def display(self, display: YGDisplay):
        self.__display = display

    @property
    def flex(self) -> float:
        return self.__flex

    @flex.setter
    def flex(self, flex: float):
        self.__flex = flex

    @property
    def flex_grow(self) -> float:
        return self.__flex_grow

    @flex_grow.setter
    def flex_grow(self, flex_grow: float):
        self.__flex_grow = flex_grow

    @property
    def flex_shrink(self) -> float:
        return self.__flex_shrink

    @flex_shrink.setter
    def flex_shrink(self, flex_shrink: float):
        self.__flex_shrink = flex_shrink

    @property
    def flex_basis(self) -> YGValue:
        return self.__flex_basis

    @flex_basis.setter
    def flex_basis(self, flex_basis: YGValue):
        self.__flex_basis = flex_basis

    @property
    def left(self) -> YGValue:
        return self.__left

    @left.setter
    def left(self, left: YGValue):
        self.__left = left

    @property
    def top(self) -> YGValue:
        return self.__top

    @top.setter
    def top(self, top: YGValue):
        self.__top = top

    @property
    def right(self) -> YGValue:
        return self.__right

    @right.setter
    def right(self, right: YGValue):
        self.__right = right

    @property
    def bottom(self) -> YGValue:
        return self.__bottom

    @bottom.setter
    def bottom(self, bottom: YGValue):
        self.__bottom = bottom

    @property
    def start(self) -> YGValue:
        return self.__start

    @start.setter
    def start(self, start: YGValue):
        self.__start = start

    @property
    def end(self) -> YGValue:
        return self.__end

    @end.setter
    def end(self, end: YGValue):
        self.__end = end

    @property
    def margin_left(self) -> YGValue:
        return self.__margin_left

    @margin_left.setter
    def margin_left(self, margin_left: YGValue):
        self.__margin_left = margin_left

    @property
    def margin_top(self) -> YGValue:
        return self.__margin_top

    @margin_top.setter
    def margin_top(self, margin_top: YGValue):
        self.__margin_top = margin_top

    @property
    def margin_right(self) -> YGValue:
        return self.__margin_right

    @margin_right.setter
    def margin_right(self, margin_right: YGValue):
        self.__margin_right = margin_right

    @property
    def margin_bottom(self) -> YGValue:
        return self.__margin_bottom

    @margin_bottom.setter
    def margin_bottom(self, margin_bottom: YGValue):
        self.__margin_bottom = margin_bottom

    @property
    def margin_start(self) -> YGValue:
        return self.__margin_start

    @margin_start.setter
    def margin_start(self, margin_start: YGValue):
        self.__margin_start = margin_start

    @property
    def margin_end(self) -> YGValue:
        return self.__margin_end

    @margin_end.setter
    def margin_end(self, margin_end: YGValue):
        self.__margin_end = margin_end

    @property
    def margin_horizontal(self) -> YGValue:
        return self.__margin_horizontal

    @margin_horizontal.setter
    def margin_horizontal(self, margin_horizontal: YGValue):
        self.__margin_horizontal = margin_horizontal

    @property
    def margin_vertical(self) -> YGValue:
        return self.__margin_vertical

    @margin_vertical.setter
    def margin_vertical(self, margin_vertical: YGValue):
        self.__margin_vertical = margin_vertical

    @property
    def margin(self) -> YGValue:
        return self.__margin

    @margin.setter
    def margin(self, margin: YGValue):
        self.__margin = margin

    @property
    def padding_left(self) -> YGValue:
        return self.__padding_left

    @padding_left.setter
    def padding_left(self, padding_left: YGValue):
        self.__padding_left = padding_left

    @property
    def padding_top(self) -> YGValue:
        return self.__padding_top

    @padding_top.setter
    def padding_top(self, padding_top: YGValue):
        self.__padding_top = padding_top

    @property
    def padding_right(self) -> YGValue:
        return self.__padding_right

    @padding_right.setter
    def padding_right(self, padding_right: YGValue):
        self.__padding_right = padding_right

    @property
    def padding_bottom(self) -> YGValue:
        return self.__padding_bottom

    @padding_bottom.setter
    def padding_bottom(self, padding_bottom: YGValue):
        self.__padding_bottom = padding_bottom

    @property
    def padding_start(self) -> YGValue:
        return self.__padding_start

    @padding_start.setter
    def padding_start(self, padding_start: YGValue):
        self.__padding_start = padding_start

    @property
    def padding_end(self) -> YGValue:
        return self.__padding_end

    @padding_end.setter
    def padding_end(self, padding_end: YGValue):
        self.__padding_end = padding_end

    @property
    def padding_horizontal(self) -> YGValue:
        return self.__padding_horizontal

    @padding_horizontal.setter
    def padding_horizontal(self, padding_horizontal: YGValue):
        self.__padding_horizontal = padding_horizontal

    @property
    def padding_vertical(self) -> YGValue:
        return self.__padding_vertical

    @padding_vertical.setter
    def padding_vertical(self, padding_vertical: YGValue):
        self.__padding_vertical = padding_vertical

    @property
    def padding(self) -> YGValue:
        return self.__padding

    @padding.setter
    def padding(self, padding: YGValue):
        self.__padding = padding

    @property
    def border_left_width(self) -> float:
        return self.__border_left_width

    @border_left_width.setter
    def border_left_width(self, border_left_width: float):
        self.__border_width = border_left_width

    @property
    def border_top_width(self) -> float:
        return self.__border_top_width

    @border_top_width.setter
    def border_top_width(self, border_top_width: float):
        self.__border_top_width = border_top_width

    @property
    def border_right_width(self) -> float:
        return self.__border_right_width

    @border_right_width.setter
    def border_right_width(self, border_right_width: float):
        self.__border_right_width = border_right_width

    @property
    def border_bottom_width(self) -> float:
        return self.__border_bottom_width

    @border_bottom_width.setter
    def border_bottom_width(self, border_bottom_width: float):
        self.__border_bottom_width = border_bottom_width

    @property
    def border_start_width(self) -> float:
        return self.__border_start_width

    @border_start_width.setter
    def border_start_width(self, border_start_width: float):
        self.__border_start_width = border_start_width

    @property
    def border_end_width(self) -> float:
        return self.__border_end_width

    @border_end_width.setter
    def border_end_width(self, border_end_width: float):
        self.__border_end_width = border_end_width

    @property
    def border_width(self) -> float:
        return self.__border_width

    @border_width.setter
    def border_width(self, border_width: float):
        self.__border_width = border_width

    @property
    def width(self) -> YGValue:
        return self.__width

    @width.setter
    def width(self, width: float):
        self.__width = width

    @property
    def height(self) -> YGValue:
        return self.__height

    @height.setter
    def height(self, height: float):
        self.__height = height

    @property
    def min_width(self) -> YGValue:
        return self.__min_width

    @min_width.setter
    def min_width(self, min_width: float):
        self.__min_width = min_width

    @property
    def min_height(self) -> YGValue:
        return self.__min_height

    @min_height.setter
    def min_height(self, min_height: float):
        self.__min_height = min_height

    @property
    def max_width(self) -> YGValue:
        return self.__max_width

    @max_width.setter
    def max_width(self, max_width: float):
        self.__max_width = max_width

    @property
    def max_height(self) -> YGValue:
        return self.__max_height

    @max_height.setter
    def max_height(self, max_height: float):
        self.__max_height = max_height

    @property
    def aspect_ratio(self) -> float:
        return self.__aspect_ratio

    @aspect_ratio.setter
    def aspect_ratio(self, aspect_ratio: float):
        self.__aspect_ratio = aspect_ratio

    @property
    def resolved_direction(self) -> YGDirection:
        pass

    def apply_layout_preserving_origin(self, preserver_origin: bool):
        pass

    def apply_layout_preserving_origin_with_dimension_flexibility(self):
        pass

    @property
    def intrinsic_size(self) -> Tuple[float, float]:
        # TODO, CAPI expose YGUndefined
        YGUndefined = 0.0
        constrained_size = [YGUndefined, YGUndefined]
        return self.calculate_layout_with_size(constrained_size)

    def calculate_layout_with_size(self, size: Tuple[float, float]) -> Tuple[float, float]:
        # TODO
        # YGAttachNodesFromViewHierachy()

        YGNodeCalculateLayout(self.__node, size[0], size[1], YGNodeStyleGetDirection(self.__node))
        return (YGNodeLayoutGetWidth(self.__node), YGNodeLayoutGetHeight(self.__node))

    @property
    def number_of_children(self) -> int:
        return YGNodeGetChildCount(self.__node)

    @property
    def is_leaf(self) -> bool:
        if self.is_enabled:
            # TODO: detect subview
            pass
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

        # TODO: target size_that_fits
        size_that_fits = [0, 0]

        return YGSize(
            PogaLayout.__sanitize_measurement__(constrained_width, size_that_fits[0], width_mode),
            PogaLayout.__sanitize_measurement__(constrained_height, size_that_fits[1], height_mode),
        )

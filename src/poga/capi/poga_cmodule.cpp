#include <Yoga.h>
#include <pybind11/pybind11.h>
#include "poga_manager.hpp"

namespace py = pybind11;
namespace poga {

std::string poga_string_version() {
    return "0.1.2";
}

std::string poga_yoga_string_version() {
    return "1.19.0";
}

PYBIND11_MODULE(libpoga_capi, m) {
    m.doc() = "pybind11 libpoga_capi plugin";  // optional module docstring

    // base
    m.def("poga_version", &poga_string_version, "return poga version.");
    m.def("poga_yoga_version", &poga_yoga_string_version,
          "return YogaLayout version.");

    m.def("YGFloatIsUndefined", &YGFloatIsUndefined);
    m.def("YGRoundValueToPixelGrid", &YGRoundValueToPixelGrid);

    // base types
    py::class_<PGNode>(m, "YGNodeRef");
    py::class_<PGConfig>(m, "YGConfigRef");
    py::class_<YGSize>(m, "YGSize")
        .def_readwrite("width", &YGSize::width)
        .def_readwrite("height", &YGSize::height);
    py::enum_<YGMeasureMode>(m, "YGMeasureMode")
        .value("Undefined", YGMeasureMode::YGMeasureModeUndefined)
        .value("Exactly", YGMeasureMode::YGMeasureModeExactly)
        .value("AtMost", YGMeasureMode::YGMeasureModeAtMost)
        .export_values();
    py::enum_<YGNodeType>(m, "YGNodeType")
        .value("Default", YGNodeType::YGNodeTypeDefault)
        .value("Text", YGNodeType::YGNodeTypeText)
        .export_values();
    py::enum_<YGDirection>(m, "YGDirection")
        .value("Inherit", YGDirection::YGDirectionInherit)
        .value("LTR", YGDirection::YGDirectionLTR)
        .value("RTL", YGDirection::YGDirectionRTL)
        .export_values();
    py::enum_<YGFlexDirection>(m, "YGFlexDirection")
        .value("Column", YGFlexDirection::YGFlexDirectionColumn)
        .value("ColumnReverse", YGFlexDirection::YGFlexDirectionColumnReverse)
        .value("Row", YGFlexDirection::YGFlexDirectionRow)
        .value("RowReverse", YGFlexDirection::YGFlexDirectionRowReverse)
        .export_values();
    py::enum_<YGJustify>(m, "YGJustify")
        .value("FlexStart", YGJustify::YGJustifyFlexStart)
        .value("Center", YGJustify::YGJustifyCenter)
        .value("FlexEnd", YGJustify::YGJustifyFlexEnd)
        .value("SpaceBetween", YGJustify::YGJustifySpaceBetween)
        .value("SpaceAround", YGJustify::YGJustifySpaceAround)
        .value("SpaceEvenly", YGJustify::YGJustifySpaceEvenly)
        .export_values();
    py::enum_<YGAlign>(m, "YGAlign")
        .value("Auto", YGAlign::YGAlignAuto)
        .value("FlexStart", YGAlign::YGAlignFlexStart)
        .value("Center", YGAlign::YGAlignCenter)
        .value("FlexEnd", YGAlign::YGAlignFlexEnd)
        .value("Stretch", YGAlign::YGAlignStretch)
        .value("Baseline", YGAlign::YGAlignBaseline)
        .value("SpaceBetween", YGAlign::YGAlignSpaceBetween)
        .value("SpaceAround", YGAlign::YGAlignSpaceAround)
        .export_values();
    py::enum_<YGDisplay>(m, "YGDisplay")
        .value("Flex", YGDisplay::YGDisplayFlex)
        .value("DisplayNone", YGDisplay::YGDisplayNone)
        .export_values();
    py::enum_<YGPositionType>(m, "YGPositionType")
        .value("Static", YGPositionType::YGPositionTypeStatic)
        .value("Relative", YGPositionType::YGPositionTypeRelative)
        .value("Absolute", YGPositionType::YGPositionTypeAbsolute)
        .export_values();
    py::enum_<YGWrap>(m, "YGWrap")
        .value("NoWrap", YGWrap::YGWrapNoWrap)
        .value("Wrap", YGWrap::YGWrapWrap)
        .value("WrapReverse", YGWrap::YGWrapWrapReverse)
        .export_values();
    py::enum_<YGOverflow>(m, "YGOverflow")
        .value("Visible", YGOverflow::YGOverflowVisible)
        .value("Hidden", YGOverflow::YGOverflowHidden)
        .value("Scroll", YGOverflow::YGOverflowScroll)
        .export_values();
    py::enum_<YGEdge>(m, "YGEdge")
        .value("Left", YGEdge::YGEdgeLeft)
        .value("Top", YGEdge::YGEdgeTop)
        .value("Right", YGEdge::YGEdgeRight)
        .value("Bottom", YGEdge::YGEdgeBottom)
        .value("Start", YGEdge::YGEdgeStart)
        .value("End", YGEdge::YGEdgeEnd)
        .value("Horizontal", YGEdge::YGEdgeHorizontal)
        .value("Vertical", YGEdge::YGEdgeVertical)
        .value("All", YGEdge::YGEdgeAll)
        .export_values();
    py::enum_<YGUnit>(m, "YGUnit")
        .value("Undefined", YGUnit::YGUnitUndefined)
        .value("Point", YGUnit::YGUnitPoint)
        .value("Percent", YGUnit::YGUnitPercent)
        .value("Auto", YGUnit::YGUnitAuto)
        .export_values();
    py::class_<YGValue>(m, "YGValue")
        .def_readwrite("value", &YGValue::value)
        .def_readwrite("unit", &YGValue::unit);
    py::enum_<YGLogLevel>(m, "YGLogLevel")
        .value("Error", YGLogLevel::YGLogLevelError)
        .value("Warn", YGLogLevel::YGLogLevelWarn)
        .value("Info", YGLogLevel::YGLogLevelInfo)
        .value("Debug", YGLogLevel::YGLogLevelDebug)
        .value("Verbose", YGLogLevel::YGLogLevelVerbose)
        .value("Fatal", YGLogLevel::YGLogLevelFatal)
        .export_values();
    py::enum_<YGExperimentalFeature>(m, "YGExperimentalFeature")
        .value("WebFlexBasis",
               YGExperimentalFeature::YGExperimentalFeatureWebFlexBasis)
        .export_values();

    // YGNode capi
    m.def("YGNodeNew", []() { return PGNode(YGNodeNew()); });
    m.def("YGNodeNewWithConfig", [](const PGConfig& config) {
        return PGNode(YGNodeNewWithConfig(config.get()));
    });
    m.def("YGNodeClone",
          [](const PGNode& node) { return PGNode(YGNodeClone(node.get())); });
    // m.def("YGNodeFreeRecursiveWithCleanupFunc",
    //     [](PGNode node) { YGNodeFreeRecursiveWithCleanupFunc(node.get(),
    //     nullptr); });
    m.def("YGNodeFree", [](const PGNode& node) {
        PogaManager::get_instance().release_node_resources(node);
        YGNodeFree(node.get());
    });
    // m.def("YGNodeFreeRecursive", [](const PGNode& node) {
    //     PogaManager::get_instance().release_node_resources(node);
    //     YGNodeFreeRecursive(node.get());
    // });
    m.def("YGNodeReset", [](const PGNode& node) { YGNodeReset(node.get()); });
    m.def("YGNodeInsertChild",
          [](const PGNode& node, const PGNode& child, uint32_t index) {
              YGNodeInsertChild(node.get(), child.get(), index);
          });
    m.def("YGNodeSwapChild",
          [](const PGNode& node, const PGNode& child, uint32_t index) {
              YGNodeSwapChild(node.get(), child.get(), index);
          });
    m.def("YGNodeRemoveChild", [](const PGNode& node, const PGNode& child) {
        YGNodeRemoveChild(node.get(), child.get());
    });
    m.def("YGNodeRemoveAllChildren",
          [](const PGNode& node) { YGNodeRemoveAllChildren(node.get()); });
    m.def("YGNodeGetChild", [](const PGNode& node, uint32_t index) {
        return PGNode(YGNodeGetChild(node.get(), index));
    });
    m.def("YGNodeGetOwner", [](const PGNode& node) {
        return PGNode(YGNodeGetOwner(node.get()));
    });
    m.def("YGNodeGetParent", [](const PGNode& node) {
        return PGNode(YGNodeGetParent(node.get()));
    });
    m.def("YGNodeGetChildCount",
          [](const PGNode& node) { return YGNodeGetChildCount(node.get()); });
    m.def("YGNodeSetChildren",
          [](const PGNode& owner, const std::vector<PGNode>& children) {
              std::vector<YGNodeRef> node_children;
              for (const auto& child : children) {
                  node_children.push_back(child.get());
              }
              YGNodeSetChildren(owner.get(), node_children);
          });
    m.def("YGNodeSetIsReferenceBaseline",
          [](const PGNode& node, bool is_reference_baseline) {
              YGNodeSetIsReferenceBaseline(node.get(), is_reference_baseline);
          });
    m.def("YGNodeIsReferenceBaseline", [](const PGNode& node) {
        return YGNodeIsReferenceBaseline(node.get());
    });
    m.def("YGNodeCalculateLayout",
          [](const PGNode& node, float available_width, float available_height,
             YGDirection owner_direction) {
              YGNodeCalculateLayout(node.get(), available_width,
                                    available_height, owner_direction);
          });
    m.def("YGNodeMarkDirty",
          [](const PGNode& node) { YGNodeMarkDirty(node.get()); });
    m.def("YGNodeMarkDirtyAndPropogateToDescendants", [](const PGNode& node) {
        YGNodeMarkDirtyAndPropogateToDescendants(node.get());
    });
    // m.def("YGNodePrint", [](PGNode node, YGPrintOptions options) {
    //     YGNodePrint(node.get(), options);
    // });
    m.def("YGNodeCanUseCachedMeasurement",
          [](YGMeasureMode width_mode, float width, YGMeasureMode height_mode,
             float height, YGMeasureMode last_width_mode, float last_width,
             YGMeasureMode last_height_mode, float last_height,
             float last_computed_width, float last_computed_height,
             float margin_row, float margin_column, const PGConfig& config) {
              return YGNodeCanUseCachedMeasurement(
                  width_mode, width, height_mode, height, last_width_mode,
                  last_width, last_height_mode, last_height,
                  last_computed_width, last_computed_height, margin_row,
                  margin_column, config.get());
          });
    m.def("YGNodeCopyStyle",
          [](const PGNode& dst_node, const PGNode& src_node) {
              YGNodeCopyStyle(dst_node.get(), src_node.get());
          });
    m.def(
        "YGNodeGetContext",
        [](const PGNode& node) {
            void* ctx = YGNodeGetContext(node.get());
            if (ctx == node.get()) {
                // ctx is poga node context
                return PogaManager::get_instance().get_node_context(node);
            }
            // otherwise is not poga node context.
            return py::object(py::none());
        },
        "Do not mix YGNodeGetContext/YGNodeSetContext in Python/C++ side");
    m.def(
        "YGNodeSetContext",
        [](const PGNode& node, const py::object& pyobj) {
            PogaManager::get_instance().set_node_context(node, pyobj);
            if (pyobj.is_none()) {
                YGNodeSetContext(node.get(), nullptr);
            } else {
                YGNodeSetContext(node.get(), node.get());
            }
        },
        "Do not mix YGNodeGetContext/YGNodeSetContext in Python/C++ side");
    m.def("YGNodeHasMeasureFunc",
          [](PGNode node) { return YGNodeHasMeasureFunc(node.get()); });
    m.def("YGNodeSetMeasureFunc", [](const PGNode& node,
                                     const py::function& func) {
        poga::PogaManager::get_instance().update_measure_method(node, func);
        if (func.is_none()) {
            YGNodeSetMeasureFunc(node.get(), nullptr);
        } else {
            YGNodeSetMeasureFunc(node.get(),
                                 poga::PogaManager::poga_measure_method);
        }
    });
    m.def("YGNodeHasBaselineFunc",
          [](const PGNode& node) { YGNodeHasBaselineFunc(node.get()); });
    m.def("YGNodeSetBaselineFunc", [](const PGNode& node,
                                      const py::function& func) {
        poga::PogaManager::get_instance().update_baseline_method(node, func);
        if (func.is_none()) {
            YGNodeSetBaselineFunc(node.get(), nullptr);
        } else {
            YGNodeSetBaselineFunc(node.get(),
                                  poga::PogaManager::poga_baseline_method);
        }
    });
    // m.def("YGNodeGetDirtiedFunc",
    //       [](const PGNode& node) { YGNodeGetDirtiedFunc(node.get()); });
    // m.def("YGNodeSetDirtiedFunc", [](const PGNode& node) {
    //     YGNodeSetDirtiedFunc(node.get(), nullptr);
    // });
    // m.def("YGNodeSetPrintFunc", [](const PGNode& node, const py::function&
    // func) {
    //     YGNodeSetPrintFunc(node.get(), func);
    // });
    m.def("YGNodeGetHasNewLayout",
          [](const PGNode& node) { return YGNodeGetHasNewLayout(node.get()); });
    m.def("YGNodeSetHasNewLayout", [](const PGNode& node, bool has_new_layout) {
        YGNodeSetHasNewLayout(node.get(), has_new_layout);
    });
    m.def("YGNodeGetNodeType",
          [](const PGNode& node) { return YGNodeGetNodeType(node.get()); });
    m.def("YGNodeSetNodeType", [](const PGNode& node, YGNodeType type) {
        YGNodeSetNodeType(node.get(), type);
    });
    m.def("YGNodeIsDirty",
          [](const PGNode& node) { return YGNodeIsDirty(node.get()); });
    m.def("YGNodeLayoutGetDidUseLegacyFlag", [](const PGNode& node) {
        return YGNodeLayoutGetDidUseLegacyFlag(node.get());
    });
    // YGNodeStyle interface
    m.def("YGNodeStyleSetDirection",
          [](const PGNode& node, YGDirection direction) {
              YGNodeStyleSetDirection(node.get(), direction);
          });
    m.def("YGNodeStyleGetDirection", [](const PGNode& node) {
        return YGNodeStyleGetDirection(node.get());
    });
    m.def("YGNodeStyleSetFlexDirection",
          [](const PGNode& node, YGFlexDirection flex_direction) {
              YGNodeStyleSetFlexDirection(node.get(), flex_direction);
          });
    m.def("YGNodeStyleGetFlexDirection", [](const PGNode& node) {
        return YGNodeStyleGetFlexDirection(node.get());
    });
    m.def("YGNodeStyleSetJustifyContent",
          [](const PGNode& node, YGJustify justify_content) {
              YGNodeStyleSetJustifyContent(node.get(), justify_content);
          });
    m.def("YGNodeStyleGetJustify", [](const PGNode& node) {
        return YGNodeStyleGetJustifyContent(
            static_cast<YGNodeConstRef>(node.get()));
    });
    m.def("YGNodeStyleSetAlignContent",
          [](const PGNode& node, YGAlign align_content) {
              YGNodeStyleSetAlignContent(node.get(), align_content);
          });
    m.def("YGNodeStyleGetAlignContent", [](const PGNode& node) {
        return YGNodeStyleGetAlignContent(
            static_cast<YGNodeConstRef>(node.get()));
    });
    m.def("YGNodeStyleSetAlignItems",
          [](const PGNode& node, YGAlign align_items) {
              YGNodeStyleSetAlignItems(node.get(), align_items);
          });
    m.def("YGNodeStyleGetAlignItems", [](const PGNode& node) {
        return YGNodeStyleGetAlignItems(
            static_cast<YGNodeConstRef>(node.get()));
    });
    m.def("YGNodeStyleSetAlignSelf",
          [](const PGNode& node, YGAlign align_self) {
              YGNodeStyleSetAlignSelf(node.get(), align_self);
          });
    m.def("YGNodeStyleGetAlignSelf", [](const PGNode& node) {
        return YGNodeStyleGetAlignSelf(static_cast<YGNodeConstRef>(node.get()));
    });
    m.def("YGNodeStyleSetPositionType",
          [](const PGNode& node, YGPositionType position_type) {
              YGNodeStyleSetPositionType(node.get(), position_type);
          });
    m.def("YGNodeStyleGetPositionType", [](const PGNode& node) {
        return YGNodeStyleGetPositionType(
            static_cast<YGNodeConstRef>(node.get()));
    });
    m.def("YGNodeStyleSetFlexWrap", [](const PGNode& node, YGWrap flex_wrap) {
        YGNodeStyleSetFlexWrap(node.get(), flex_wrap);
    });
    m.def("YGNodeStyleGetFlexWrap", [](const PGNode& node) {
        return YGNodeStyleGetFlexWrap(static_cast<YGNodeConstRef>(node.get()));
    });
    m.def("YGNodeStyleSetOverflow",
          [](const PGNode& node, YGOverflow overflow) {
              YGNodeStyleSetOverflow(node.get(), overflow);
          });
    m.def("YGNodeStyleGetOverflow", [](const PGNode& node) {
        return YGNodeStyleGetOverflow(static_cast<YGNodeConstRef>(node.get()));
    });
    m.def("YGNodeStyleSetDisplay", [](const PGNode& node, YGDisplay display) {
        YGNodeStyleSetDisplay(node.get(), display);
    });
    m.def("YGNodeStyleGetDisplay", [](const PGNode& node) {
        return YGNodeStyleGetDisplay(static_cast<YGNodeConstRef>(node.get()));
    });
    m.def("YGNodeStyleSetFlex", [](const PGNode& node, float flex) {
        YGNodeStyleSetFlex(node.get(), flex);
    });
    m.def("YGNodeStyleGetFlex", [](const PGNode& node) {
        return YGNodeStyleGetFlex(static_cast<YGNodeConstRef>(node.get()));
    });
    m.def("YGNodeStyleSetFlexGrow", [](const PGNode& node, float flex_grow) {
        YGNodeStyleSetFlexGrow(node.get(), flex_grow);
    });
    m.def("YGNodeStyleGetFlexGrow", [](const PGNode& node) {
        return YGNodeStyleGetFlexGrow(static_cast<YGNodeConstRef>(node.get()));
    });
    m.def("YGNodeStyleSetFlexShrink",
          [](const PGNode& node, float flex_shrink) {
              YGNodeStyleSetFlexShrink(node.get(), flex_shrink);
          });
    m.def("YGNodeStyleGetFlexShrink", [](const PGNode& node) {
        return YGNodeStyleGetFlexShrink(
            static_cast<YGNodeConstRef>(node.get()));
    });
    m.def("YGNodeStyleSetFlexBasis", [](const PGNode& node, float flex_basis) {
        YGNodeStyleSetFlexBasis(node.get(), flex_basis);
    });
    m.def("YGNodeStyleSetFlexBasisPercent",
          [](const PGNode& node, float flex_basis) {
              YGNodeStyleSetFlexBasisPercent(node.get(), flex_basis);
          });
    m.def("YGNodeStyleSetFlexBasisAuto",
          [](const PGNode& node) {
              YGNodeStyleSetFlexBasisAuto(node.get());
          });
    m.def("YGNodeStyleGetFlexBasis", [](const PGNode& node) {
        return YGNodeStyleGetFlexBasis(static_cast<YGNodeConstRef>(node.get()));
    });
    m.def("YGNodeStyleSetPosition",
          [](const PGNode& node, YGEdge edge, float position) {
              YGNodeStyleSetPosition(node.get(), edge, position);
          });
    m.def("YGNodeStyleSetPositionPercent",
          [](const PGNode& node, YGEdge edge, float position) {
              YGNodeStyleSetPositionPercent(node.get(), edge, position);
          });
    m.def("YGNodeStyleGetPosition", [](const PGNode& node, YGEdge edge) {
        return YGNodeStyleGetPosition(static_cast<YGNodeConstRef>(node.get()),
                                      edge);
    });
    m.def("YGNodeStyleSetMargin",
          [](const PGNode& node, YGEdge edge, float margin) {
              YGNodeStyleSetMargin(node.get(), edge, margin);
          });
    m.def("YGNodeStyleSetMarginPercent",
          [](const PGNode& node, YGEdge edge, float margin) {
              YGNodeStyleSetMarginPercent(node.get(), edge, margin);
          });
    m.def("YGNodeStyleSetMarginAuto", [](const PGNode& node, YGEdge edge) {
        YGNodeStyleSetMarginAuto(node.get(), edge);
    });
    m.def("YGNodeStyleGetMargin", [](const PGNode& node, YGEdge edge) {
        return YGNodeStyleGetMargin(node.get(), edge);
    });
    m.def("YGNodeStyleSetPadding",
          [](const PGNode& node, YGEdge edge, float padding) {
              YGNodeStyleSetPadding(node.get(), edge, padding);
          });
    m.def("YGNodeStyleSetPaddingPercent",
          [](const PGNode& node, YGEdge edge, float padding) {
              YGNodeStyleSetPaddingPercent(node.get(), edge, padding);
          });
    m.def("YGNodeStyleGetPadding", [](const PGNode& node, YGEdge edge) {
        return YGNodeStyleGetPadding(node.get(), edge);
    });
    m.def("YGNodeStyleSetBorder",
          [](const PGNode& node, YGEdge edge, float border) {
              YGNodeStyleSetBorder(node.get(), edge, border);
          });
    m.def("YGNodeStyleGetBorder", [](const PGNode& node, YGEdge edge) {
        return YGNodeStyleGetBorder(node.get(), edge);
    });
    m.def("YGNodeStyleSetWidth", [](const PGNode& node, float width) {
        YGNodeStyleSetWidth(node.get(), width);
    });
    m.def("YGNodeStyleSetWidthPercent", [](const PGNode& node, float width) {
        YGNodeStyleSetWidthPercent(node.get(), width);
    });
    m.def("YGNodeStyleSetWidthAuto",
          [](const PGNode& node) { YGNodeStyleSetWidthAuto(node.get()); });
    m.def("YGNodeStyleGetWidth",
          [](const PGNode& node) { return YGNodeStyleGetWidth(node.get()); });

    m.def("YGNodeStyleSetHeight", [](const PGNode& node, float height) {
        YGNodeStyleSetHeight(node.get(), height);
    });
    m.def("YGNodeStyleSetHeightPercent", [](const PGNode& node, float height) {
        YGNodeStyleSetHeightPercent(node.get(), height);
    });
    m.def("YGNodeStyleSetHeightAuto",
          [](const PGNode& node) { YGNodeStyleSetHeightAuto(node.get()); });
    m.def("YGNodeStyleGetHeight",
          [](const PGNode& node) { return YGNodeStyleGetHeight(node.get()); });

    m.def("YGNodeStyleSetMinWidth", [](const PGNode& node, float min_width) {
        YGNodeStyleSetMinWidth(node.get(), min_width);
    });
    m.def("YGNodeStyleSetMinWidthPercent",
          [](const PGNode& node, float min_width) {
              YGNodeStyleSetMinWidthPercent(node.get(), min_width);
          });
    m.def("YGNodeStyleGetMinWidth", [](const PGNode& node) {
        return YGNodeStyleGetMinWidth(node.get());
    });

    m.def("YGNodeStyleSetMinHeight", [](const PGNode& node, float min_height) {
        YGNodeStyleSetMinHeight(node.get(), min_height);
    });
    m.def("YGNodeStyleSetMinHeightPercent",
          [](const PGNode& node, float min_height) {
              YGNodeStyleSetMinHeightPercent(node.get(), min_height);
          });
    m.def("YGNodeStyleGetMinHeight", [](const PGNode& node) {
        return YGNodeStyleGetMinHeight(node.get());
    });

    m.def("YGNodeStyleSetMaxHeight", [](const PGNode& node, float max_height) {
        YGNodeStyleSetMaxHeight(node.get(), max_height);
    });
    m.def("YGNodeStyleSetMaxHeightPercent",
          [](const PGNode& node, float max_height) {
              YGNodeStyleSetMaxHeightPercent(node.get(), max_height);
          });
    m.def("YGNodeStyleGetMaxHeight", [](const PGNode& node) {
        return YGNodeStyleGetMaxHeight(node.get());
    });

    m.def("YGNodeStyleSetAspectRatio",
          [](const PGNode& node, float aspect_ratio) {
              return YGNodeStyleSetAspectRatio(node.get(), aspect_ratio);
          });
    m.def("YGNodeStyleGetAspectRatio", [](const PGNode& node) {
        return YGNodeStyleGetAspectRatio(node.get());
    });

    // YGNodeLayout interface
    m.def("YGNodeLayoutGetLeft",
          [](const PGNode& node) { return YGNodeLayoutGetLeft(node.get()); });
    m.def("YGNodeLayoutGetTop",
          [](const PGNode& node) { return YGNodeLayoutGetTop(node.get()); });
    m.def("YGNodeLayoutGetRight",
          [](const PGNode& node) { return YGNodeLayoutGetRight(node.get()); });
    m.def("YGNodeLayoutGetBottom",
          [](const PGNode& node) { return YGNodeLayoutGetBottom(node.get()); });
    m.def("YGNodeLayoutGetWidth",
          [](const PGNode& node) { return YGNodeLayoutGetWidth(node.get()); });
    m.def("YGNodeLayoutGetHeight",
          [](const PGNode& node) { return YGNodeLayoutGetHeight(node.get()); });
    m.def("YGNodeLayoutGetDirection", [](const PGNode& node) {
        return YGNodeLayoutGetDirection(node.get());
    });
    m.def("YGNodeLayoutGetHadOverflow", [](const PGNode& node) {
        return YGNodeLayoutGetHadOverflow(node.get());
    });
    m.def(
        "YGNodeLayoutGetDidLegacyStretchFlagAffectLayout",
        [](const PGNode& node) {
            return YGNodeLayoutGetDidLegacyStretchFlagAffectLayout(node.get());
        });

    m.def("YGNodeLayoutGetMargin", [](const PGNode& node, YGEdge edge) {
        return YGNodeLayoutGetMargin(node.get(), edge);
    });
    m.def("YGNodeLayoutGetBorder", [](const PGNode& node, YGEdge edge) {
        return YGNodeLayoutGetBorder(node.get(), edge);
    });
    m.def("YGNodeLayoutGetPadding", [](const PGNode& node, YGEdge edge) {
        return YGNodeLayoutGetPadding(node.get(), edge);
    });

    // YGConfig interface
    m.def("YGConfigSetLogger", [](const PGConfig& config,
                                  const py::function& func) {
        poga::PogaManager::get_instance().update_config_logger_method(
            config.get(), func);
        if (func.is_none()) {
            YGConfigSetLogger(config.get(), nullptr);
        } else {
            YGConfigSetLogger(config.get(),
                              poga::PogaManager::poga_config_logger_method);
        }
    });
    m.def("YGConfigSetPrintTreeFlag", [](const PGConfig& config, bool enabled) {
        YGConfigSetPrintTreeFlag(config.get(), enabled);
    });
    m.def("YGConfigSetPointScaleFactor",
          [](const PGConfig& config, float pixels_in_point) {
              YGConfigSetPointScaleFactor(config.get(), pixels_in_point);
          });
    m.def("YGConfigSetShouldDiffLayoutWithoutLegacyStretchBehaviour",
          [](const PGConfig& config, bool should_diff_layout) {
              YGConfigSetShouldDiffLayoutWithoutLegacyStretchBehaviour(
                  config.get(), should_diff_layout);
          });
    m.def("YGConfigSetUseLegacyStretchBehaviour",
          [](const PGConfig& config, bool use_legacy_stretch_behaviour) {
              YGConfigSetUseLegacyStretchBehaviour(
                  config.get(), use_legacy_stretch_behaviour);
          });
    m.def("YGConfigNew", []() { return PGConfig(YGConfigNew()); });
    m.def("YGConfigFree", [](const PGConfig& config) {
        poga::PogaManager::get_instance().release_config_resources(config);
        YGConfigFree(config.get());
    });
    m.def("YGConfigCopy", [](const PGConfig& dest, const PGConfig& src) {
        YGConfigCopy(dest.get(), src.get());
    });
    m.def("YGConfigGetInstanceCount",
          []() { return YGConfigGetInstanceCount(); });
    m.def("YGConfigSetExperimentalFeatureEnabled",
          [](const PGConfig& config, YGExperimentalFeature feature,
             bool enabled) {
              YGConfigSetExperimentalFeatureEnabled(config.get(),
                                                           feature, enabled);
          });
    // m.def("YGConfigIsExperimentalFeatureEnabled",
    //       [](const PGConfig& config, YGExperimentalFeature feature) {
    //           return YGConfigIsExperimentalFeatureEnabled(config.get(),
    //                                                       feature);
    //       });
    m.def("YGConfigSetUseWebDefaults",
          [](const PGConfig& config, bool enabled) {
              YGConfigSetUseWebDefaults(config.get(), enabled);
          });
    m.def("YGConfigGetUseWebDefaults", [](const PGConfig& config) {
        return YGConfigGetUseWebDefaults(config.get());
    });
    // TODO: config clone node callback without config object.
    // m.def("YGConfigSetCloneNodeFunc", [](const PGConfig& config,
    //                                      const py::function& func) {
    //     poga::PogaManager::get_instance().update_config_clone_node_method(func);
    //     if (func.is_none()) {
    //         YGConfigSetCloneNodeFunc(config.get(), nullptr);
    //     } else {
    //         YGConfigSetCloneNodeFunc(
    //             config.get(),
    //             poga::PogaManager::poga_config_clone_node_method);
    //     }
    // });
}

}  // namespace poga

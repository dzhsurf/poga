#include <Yoga.h>
#include <pybind11/pybind11.h>
#include "poga_manager.hpp"

namespace py = pybind11;
namespace poga {

std::string poga_string_version() {
    return "0.1.0";
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
    m.def("YGNodeSetMeasureFunc",
          [](const PGNode& node, const py::function& measure_func) {
              poga::PogaManager::get_instance().update_measure_method(
                  node, measure_func);
              if (measure_func.is_none()) {
                  YGNodeSetMeasureFunc(node.get(), nullptr);
              } else {
                  YGNodeSetMeasureFunc(node.get(),
                                       poga::PogaManager::poga_measure_method);
              }
          });
}

}  // namespace poga

//     {"ygnode_set_measure_func", (PyCFunction)NULL, METH_VARARGS},
//     {"ygnode_has_baseline_func", (PyCFunction)NULL, METH_VARARGS},
//     {"ygnode_set_baseline_func", (PyCFunction)NULL, METH_VARARGS},
//     {"ygnode_get_dirtied_func", (PyCFunction)NULL, METH_VARARGS},
//     {"ygnode_set_dirtied_func", (PyCFunction)NULL, METH_VARARGS},
//     {"ygnode_set_print_func", (PyCFunction)NULL, METH_VARARGS},
//     {"ygnode_get_has_new_layout", (PyCFunction)NULL, METH_VARARGS},
//     {"ygnode_set_has_new_layout", (PyCFunction)NULL, METH_VARARGS},
//     {"ygnode_get_node_type", (PyCFunction)NULL, METH_VARARGS},
//     {"ygnode_set_node_type", (PyCFunction)NULL, METH_VARARGS},
//     {"ygnode_is_dirty", (PyCFunction)NULL, METH_VARARGS},
//     {"ygnode_layout_get_did_use_legacy_flag", (PyCFunction)NULL,
//     METH_VARARGS},

//     {"ygnode_style_set_direction", (PyCFunction)NULL, METH_VARARGS},
//     {"ygnode_style_get_direction", (PyCFunction)NULL, METH_VARARGS},
//     {"ygnode_style_set_flex_direction", (PyCFunction)NULL, METH_VARARGS},
//     {"ygnode_style_get_flex_direction", (PyCFunction)NULL, METH_VARARGS},
//     {"ygnode_style_set_justify_content", (PyCFunction)NULL, METH_VARARGS},
//     {"ygnode_style_get_justify)content", (PyCFunction)NULL, METH_VARARGS},
//     {"ygnode_style_set_align_content", (PyCFunction)NULL, METH_VARARGS},
//     {"ygnode_style_get_align_content", (PyCFunction)NULL, METH_VARARGS},
//     {"ygnode_style_set_align_items", (PyCFunction)NULL, METH_VARARGS},
//     {"ygnode_style_get_align_items", (PyCFunction)NULL, METH_VARARGS},
//     {"ygnode_style_set_align_self", (PyCFunction)NULL, METH_VARARGS},
//     {"ygnode_style_get_align_self", (PyCFunction)NULL, METH_VARARGS},
//     {"ygnode_style_set_position_type", (PyCFunction)NULL, METH_VARARGS},
//     {"ygnode_style_get_position_type", (PyCFunction)NULL, METH_VARARGS},
//     {"ygnode_style_set_flex_wrap", (PyCFunction)NULL, METH_VARARGS},
//     {"ygnode_style_get_flex_wrap", (PyCFunction)NULL, METH_VARARGS},
//     {"ygnode_style_set_overflow", (PyCFunction)NULL, METH_VARARGS},
//     {"ygnode_style_get_overflow", (PyCFunction)NULL, METH_VARARGS},
//     {"ygnode_style_set_display", (PyCFunction)NULL, METH_VARARGS},
//     {"ygnode_style_get_display", (PyCFunction)NULL, METH_VARARGS},
//     {"ygnode_style_set_flex", (PyCFunction)NULL, METH_VARARGS},
//     {"ygnode_style_get_flex", (PyCFunction)NULL, METH_VARARGS},
//     {"ygnode_style_set_flex_grow", (PyCFunction)NULL, METH_VARARGS},
//     {"ygnode_style_get_flex_grow", (PyCFunction)NULL, METH_VARARGS},
//     {"ygnode_style_set_flex_shink", (PyCFunction)NULL, METH_VARARGS},
//     {"ygnode_style_get_flex_shink", (PyCFunction)NULL, METH_VARARGS},
//     {"ygnode_style_set_flex_basis", (PyCFunction)NULL, METH_VARARGS},
//     {"ygnode_style_set_flex_basis_percent", (PyCFunction)NULL, METH_VARARGS},
//     {"ygnode_style_set_flex_basis_auto", (PyCFunction)NULL, METH_VARARGS},
//     {"ygnode_style_get_flex_basis", (PyCFunction)NULL, METH_VARARGS},
//     {"ygnode_style_set_position", (PyCFunction)NULL, METH_VARARGS},
//     {"ygnode_style_set_position_percent", (PyCFunction)NULL, METH_VARARGS},
//     {"ygnode_style_get_position", (PyCFunction)NULL, METH_VARARGS},
//     {"ygnode_style_set_margin", (PyCFunction)NULL, METH_VARARGS},
//     {"ygnode_style_set_margin_percent", (PyCFunction)NULL, METH_VARARGS},
//     {"ygnode_style_set_margin_auto", (PyCFunction)NULL, METH_VARARGS},
//     {"ygnode_style_get_margin", (PyCFunction)NULL, METH_VARARGS},
//     {"ygnode_style_set_padding", (PyCFunction)NULL, METH_VARARGS},
//     {"ygnode_style_set_padding_percent", (PyCFunction)NULL, METH_VARARGS},
//     {"ygnode_style_get_padding", (PyCFunction)NULL, METH_VARARGS},
//     {"ygnode_style_set_border", (PyCFunction)NULL, METH_VARARGS},
//     {"ygnode_style_get_border", (PyCFunction)NULL, METH_VARARGS},
//     {"ygnode_style_set_width", (PyCFunction)NULL, METH_VARARGS},
//     {"ygnode_style_set_width_percent", (PyCFunction)NULL, METH_VARARGS},
//     {"ygnode_style_set_width_auto", (PyCFunction)NULL, METH_VARARGS},
//     {"ygnode_style_get_width", (PyCFunction)NULL, METH_VARARGS},
//     {"ygnode_style_set_height", (PyCFunction)NULL, METH_VARARGS},
//     {"ygnode_style_set_height_percent", (PyCFunction)NULL, METH_VARARGS},
//     {"ygnode_style_set_height_auto", (PyCFunction)NULL, METH_VARARGS},
//     {"ygnode_style_get_height", (PyCFunction)NULL, METH_VARARGS},
//     {"ygnode_style_set_min_width", (PyCFunction)NULL, METH_VARARGS},
//     {"ygnode_style_set_min_width_percent", (PyCFunction)NULL, METH_VARARGS},
//     {"ygnode_style_get_min_width", (PyCFunction)NULL, METH_VARARGS},
//     {"ygnode_style_set_min_height", (PyCFunction)NULL, METH_VARARGS},
//     {"ygnode_style_set_min_height_percent", (PyCFunction)NULL, METH_VARARGS},
//     {"ygnode_style_get_min_height", (PyCFunction)NULL, METH_VARARGS},
//     {"ygnode_style_set_max_height", (PyCFunction)NULL, METH_VARARGS},
//     {"ygnode_style_set_max_height_percent", (PyCFunction)NULL, METH_VARARGS},
//     {"ygnode_style_get_max_height", (PyCFunction)NULL, METH_VARARGS},
//     {"ygnode_style_set_aspect_ratio", (PyCFunction)NULL, METH_VARARGS},
//     {"ygnode_style_get_aspect_ratio", (PyCFunction)NULL, METH_VARARGS},
//     {"ygnode_layout_get_left", (PyCFunction)NULL, METH_VARARGS},
//     {"ygnode_layout_get_top", (PyCFunction)NULL, METH_VARARGS},
//     {"ygnode_layout_get_right", (PyCFunction)NULL, METH_VARARGS},
//     {"ygnode_layout_get_botttom", (PyCFunction)NULL, METH_VARARGS},
//     {"ygnode_layout_get_width", (PyCFunction)NULL, METH_VARARGS},
//     {"ygnode_layout_get_height", (PyCFunction)NULL, METH_VARARGS},
//     {"ygnode_layout_get_direction", (PyCFunction)NULL, METH_VARARGS},
//     {"ygnode_layout_get_had_overflow", (PyCFunction)NULL, METH_VARARGS},
//     {"ygnode_layout_get_did_legacy_stretch_flag_affect_layout",
//      (PyCFunction)NULL, METH_VARARGS},
//     {"ygnode_layout_get_margin", (PyCFunction)NULL, METH_VARARGS},
//     {"ygnode_layout_get_border", (PyCFunction)NULL, METH_VARARGS},
//     {"ygnode_layout_get_padding", (PyCFunction)NULL, METH_VARARGS},

//     // YGConfig
//     {"ygconfig_set_logger", (PyCFunction)NULL, METH_VARARGS},
//     {"ygconfig_set_print_tree_flag", (PyCFunction)NULL, METH_VARARGS},
//     {"ygconfig_set_point_scale_factor", (PyCFunction)NULL, METH_VARARGS},
//     {"ygconfig_set_should_diff_layout_without_legacu_stretch_behaviour",
//      (PyCFunction)NULL, METH_VARARGS},
//     {"ygconfig_set_use_legacy_stretch_behaviour", (PyCFunction)NULL,
//      METH_VARARGS},
//     {"ygconfig_new", (PyCFunction)NULL, METH_NOARGS},
//     {"ygconfig_free", (PyCFunction)NULL, METH_VARARGS},
//     {"ygconfig_copy", (PyCFunction)NULL, METH_VARARGS},
//     {"ygconfig_get_instance_count", (PyCFunction)NULL, METH_NOARGS},
//     {"ygconfig_set_experimental_feature_enabled", (PyCFunction)NULL,
//      METH_VARARGS},
//     {"ygconfig_is_experimental_feature_enabled", (PyCFunction)NULL,
//      METH_VARARGS},
//     {"ygconfig_set_use_web_defaults", (PyCFunction)NULL, METH_VARARGS},
//     {"ygconfig_get_use_web_defaults", (PyCFunction)NULL, METH_VARARGS},
//     {"ygconfig_set_clone_node_func", (PyCFunction)NULL, METH_VARARGS},

//     {NULL, NULL, 0, NULL},
// };
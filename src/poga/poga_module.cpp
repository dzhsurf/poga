#define PY_SSIZE_T_CLEAN
#include <Python.h>

#include "internal/capi_binding.h"
#include "internal/private.h"
#include "internal/types.h"
#include "poga.h"

#ifdef __cplusplus
extern "C" {
#endif

static Poga_CAPI_t CAPI = {
    &PogaYGNodeRef_Type,  // PyTypeObject *YGNodeRef_Type;
};

static PyObject* poga_version(PyObject* self, PyObject* ignored) {
    return PyLong_FromLong(0);
}

static PyObject* poga_version_string(PyObject* self, PyObject* ignored) {
    return PyUnicode_FromString("0.1.0");
}

static PyObject* poga_float_is_undefined(PyObject* self, PyObject* args) {
    double value = 0.0;
    if (!PyArg_ParseTuple(args, "yoga_float_is_undefined", &value))
        return NULL;

    bool ret = YGFloatIsUndefined(value);
    return PyBool_FromLong(ret ? 1 : 0);
}

static PyObject* poga_round_value_to_pixel_grid(PyObject* self,
                                                PyObject* args) {
    return PyLong_FromLong(0);
}

static PyMethodDef poga_functions[] = {
    {"yoga_version", (PyCFunction)poga_version, METH_NOARGS},
    {"yoga_version_string", (PyCFunction)poga_version_string, METH_NOARGS},
    {"yoga_float_is_undefined", (PyCFunction)poga_float_is_undefined,
     METH_VARARGS},
    {"yoga_round_value_to_pixel_grid",
     (PyCFunction)poga_round_value_to_pixel_grid, METH_VARARGS},

    // YGNode
    {"ygnode_new", (PyCFunction)poga_ygnode_new, METH_NOARGS},
    {"ygnode_new_with_config", (PyCFunction)NULL, METH_VARARGS},
    {"ygnode_clone", (PyCFunction)NULL, METH_VARARGS},
    {"ygnode_free", (PyCFunction)NULL, METH_VARARGS},
    {"ygnode_free_recursive_with_cleanup_func", (PyCFunction)NULL,
     METH_VARARGS},
    {"ygnode_free_recursive", (PyCFunction)NULL, METH_VARARGS},
    {"ygnode_reset", (PyCFunction)NULL, METH_VARARGS},
    {"ygnode_insert_child", (PyCFunction)NULL, METH_VARARGS},
    {"ygnode_swap_child", (PyCFunction)NULL, METH_VARARGS},
    {"ygnode_remove_child", (PyCFunction)NULL, METH_VARARGS},
    {"ygnode_remove_all_children", (PyCFunction)NULL, METH_VARARGS},
    {"ygnode_get_child", (PyCFunction)NULL, METH_VARARGS},
    {"ygnode_get_owner", (PyCFunction)NULL, METH_VARARGS},
    {"ygnode_get_parent", (PyCFunction)NULL, METH_VARARGS},
    {"ygnode_get_child_count", (PyCFunction)NULL, METH_VARARGS},
    {"ygnode_set_children", (PyCFunction)NULL, METH_VARARGS},
    {"ygnode_set_is_reference_baseline", (PyCFunction)NULL, METH_VARARGS},
    {"ygnode_is_reference_baseline", (PyCFunction)NULL, METH_VARARGS},
    {"ygnode_calculate_layout", (PyCFunction)NULL, METH_VARARGS},
    {"ygnode_mark_dirty", (PyCFunction)NULL, METH_VARARGS},
    {"ygnode_mark_dirty_and_propogate_to_descendants", (PyCFunction)NULL,
     METH_VARARGS},
    {"ygnode_print", (PyCFunction)NULL, METH_VARARGS},
    {"ygnode_can_use_cached_measurement", (PyCFunction)NULL, METH_VARARGS},
    {"ygnode_copy_style", (PyCFunction)NULL, METH_VARARGS},
    {"ygnode_get_context", (PyCFunction)NULL, METH_VARARGS},
    {"ygnode_set_context", (PyCFunction)NULL, METH_VARARGS},
    {"ygnode_has_measure_func", (PyCFunction)NULL, METH_VARARGS},
    {"ygnode_set_measure_func", (PyCFunction)NULL, METH_VARARGS},
    {"ygnode_has_baseline_func", (PyCFunction)NULL, METH_VARARGS},
    {"ygnode_set_baseline_func", (PyCFunction)NULL, METH_VARARGS},
    {"ygnode_get_dirtied_func", (PyCFunction)NULL, METH_VARARGS},
    {"ygnode_set_dirtied_func", (PyCFunction)NULL, METH_VARARGS},
    {"ygnode_set_print_func", (PyCFunction)NULL, METH_VARARGS},
    {"ygnode_get_has_new_layout", (PyCFunction)NULL, METH_VARARGS},
    {"ygnode_set_has_new_layout", (PyCFunction)NULL, METH_VARARGS},
    {"ygnode_get_node_type", (PyCFunction)NULL, METH_VARARGS},
    {"ygnode_set_node_type", (PyCFunction)NULL, METH_VARARGS},
    {"ygnode_is_dirty", (PyCFunction)NULL, METH_VARARGS},
    {"ygnode_layout_get_did_use_legacy_flag", (PyCFunction)NULL, METH_VARARGS},

    {"ygnode_style_set_direction", (PyCFunction)NULL, METH_VARARGS},
    {"ygnode_style_get_direction", (PyCFunction)NULL, METH_VARARGS},
    {"ygnode_style_set_flex_direction", (PyCFunction)NULL, METH_VARARGS},
    {"ygnode_style_get_flex_direction", (PyCFunction)NULL, METH_VARARGS},
    {"ygnode_style_set_justify_content", (PyCFunction)NULL, METH_VARARGS},
    {"ygnode_style_get_justify)content", (PyCFunction)NULL, METH_VARARGS},
    {"ygnode_style_set_align_content", (PyCFunction)NULL, METH_VARARGS},
    {"ygnode_style_get_align_content", (PyCFunction)NULL, METH_VARARGS},
    {"ygnode_style_set_align_items", (PyCFunction)NULL, METH_VARARGS},
    {"ygnode_style_get_align_items", (PyCFunction)NULL, METH_VARARGS},
    {"ygnode_style_set_align_self", (PyCFunction)NULL, METH_VARARGS},
    {"ygnode_style_get_align_self", (PyCFunction)NULL, METH_VARARGS},
    {"ygnode_style_set_position_type", (PyCFunction)NULL, METH_VARARGS},
    {"ygnode_style_get_position_type", (PyCFunction)NULL, METH_VARARGS},
    {"ygnode_style_set_flex_wrap", (PyCFunction)NULL, METH_VARARGS},
    {"ygnode_style_get_flex_wrap", (PyCFunction)NULL, METH_VARARGS},
    {"ygnode_style_set_overflow", (PyCFunction)NULL, METH_VARARGS},
    {"ygnode_style_get_overflow", (PyCFunction)NULL, METH_VARARGS},
    {"ygnode_style_set_display", (PyCFunction)NULL, METH_VARARGS},
    {"ygnode_style_get_display", (PyCFunction)NULL, METH_VARARGS},
    {"ygnode_style_set_flex", (PyCFunction)NULL, METH_VARARGS},
    {"ygnode_style_get_flex", (PyCFunction)NULL, METH_VARARGS},
    {"ygnode_style_set_flex_grow", (PyCFunction)NULL, METH_VARARGS},
    {"ygnode_style_get_flex_grow", (PyCFunction)NULL, METH_VARARGS},
    {"ygnode_style_set_flex_shink", (PyCFunction)NULL, METH_VARARGS},
    {"ygnode_style_get_flex_shink", (PyCFunction)NULL, METH_VARARGS},
    {"ygnode_style_set_flex_basis", (PyCFunction)NULL, METH_VARARGS},
    {"ygnode_style_set_flex_basis_percent", (PyCFunction)NULL, METH_VARARGS},
    {"ygnode_style_set_flex_basis_auto", (PyCFunction)NULL, METH_VARARGS},
    {"ygnode_style_get_flex_basis", (PyCFunction)NULL, METH_VARARGS},
    {"ygnode_style_set_position", (PyCFunction)NULL, METH_VARARGS},
    {"ygnode_style_set_position_percent", (PyCFunction)NULL, METH_VARARGS},
    {"ygnode_style_get_position", (PyCFunction)NULL, METH_VARARGS},
    {"ygnode_style_set_margin", (PyCFunction)NULL, METH_VARARGS},
    {"ygnode_style_set_margin_percent", (PyCFunction)NULL, METH_VARARGS},
    {"ygnode_style_set_margin_auto", (PyCFunction)NULL, METH_VARARGS},
    {"ygnode_style_get_margin", (PyCFunction)NULL, METH_VARARGS},
    {"ygnode_style_set_padding", (PyCFunction)NULL, METH_VARARGS},
    {"ygnode_style_set_padding_percent", (PyCFunction)NULL, METH_VARARGS},
    {"ygnode_style_get_padding", (PyCFunction)NULL, METH_VARARGS},
    {"ygnode_style_set_border", (PyCFunction)NULL, METH_VARARGS},
    {"ygnode_style_get_border", (PyCFunction)NULL, METH_VARARGS},
    {"ygnode_style_set_width", (PyCFunction)NULL, METH_VARARGS},
    {"ygnode_style_set_width_percent", (PyCFunction)NULL, METH_VARARGS},
    {"ygnode_style_set_width_auto", (PyCFunction)NULL, METH_VARARGS},
    {"ygnode_style_get_width", (PyCFunction)NULL, METH_VARARGS},
    {"ygnode_style_set_height", (PyCFunction)NULL, METH_VARARGS},
    {"ygnode_style_set_height_percent", (PyCFunction)NULL, METH_VARARGS},
    {"ygnode_style_set_height_auto", (PyCFunction)NULL, METH_VARARGS},
    {"ygnode_style_get_height", (PyCFunction)NULL, METH_VARARGS},
    {"ygnode_style_set_min_width", (PyCFunction)NULL, METH_VARARGS},
    {"ygnode_style_set_min_width_percent", (PyCFunction)NULL, METH_VARARGS},
    {"ygnode_style_get_min_width", (PyCFunction)NULL, METH_VARARGS},
    {"ygnode_style_set_min_height", (PyCFunction)NULL, METH_VARARGS},
    {"ygnode_style_set_min_height_percent", (PyCFunction)NULL, METH_VARARGS},
    {"ygnode_style_get_min_height", (PyCFunction)NULL, METH_VARARGS},
    {"ygnode_style_set_max_height", (PyCFunction)NULL, METH_VARARGS},
    {"ygnode_style_set_max_height_percent", (PyCFunction)NULL, METH_VARARGS},
    {"ygnode_style_get_max_height", (PyCFunction)NULL, METH_VARARGS},
    {"ygnode_style_set_aspect_ratio", (PyCFunction)NULL, METH_VARARGS},
    {"ygnode_style_get_aspect_ratio", (PyCFunction)NULL, METH_VARARGS},
    {"ygnode_layout_get_left", (PyCFunction)NULL, METH_VARARGS},
    {"ygnode_layout_get_top", (PyCFunction)NULL, METH_VARARGS},
    {"ygnode_layout_get_right", (PyCFunction)NULL, METH_VARARGS},
    {"ygnode_layout_get_botttom", (PyCFunction)NULL, METH_VARARGS},
    {"ygnode_layout_get_width", (PyCFunction)NULL, METH_VARARGS},
    {"ygnode_layout_get_height", (PyCFunction)NULL, METH_VARARGS},
    {"ygnode_layout_get_direction", (PyCFunction)NULL, METH_VARARGS},
    {"ygnode_layout_get_had_overflow", (PyCFunction)NULL, METH_VARARGS},
    {"ygnode_layout_get_did_legacy_stretch_flag_affect_layout",
     (PyCFunction)NULL, METH_VARARGS},
    {"ygnode_layout_get_margin", (PyCFunction)NULL, METH_VARARGS},
    {"ygnode_layout_get_border", (PyCFunction)NULL, METH_VARARGS},
    {"ygnode_layout_get_padding", (PyCFunction)NULL, METH_VARARGS},

    // YGConfig
    {"ygconfig_set_logger", (PyCFunction)NULL, METH_VARARGS},
    {"ygconfig_set_print_tree_flag", (PyCFunction)NULL, METH_VARARGS},
    {"ygconfig_set_point_scale_factor", (PyCFunction)NULL, METH_VARARGS},
    {"ygconfig_set_should_diff_layout_without_legacu_stretch_behaviour",
     (PyCFunction)NULL, METH_VARARGS},
    {"ygconfig_set_use_legacy_stretch_behaviour", (PyCFunction)NULL,
     METH_VARARGS},
    {"ygconfig_new", (PyCFunction)NULL, METH_NOARGS},
    {"ygconfig_free", (PyCFunction)NULL, METH_VARARGS},
    {"ygconfig_copy", (PyCFunction)NULL, METH_VARARGS},
    {"ygconfig_get_instance_count", (PyCFunction)NULL, METH_NOARGS},
    {"ygconfig_set_experimental_feature_enabled", (PyCFunction)NULL,
     METH_VARARGS},
    {"ygconfig_is_experimental_feature_enabled", (PyCFunction)NULL,
     METH_VARARGS},
    {"ygconfig_set_use_web_defaults", (PyCFunction)NULL, METH_VARARGS},
    {"ygconfig_get_use_web_defaults", (PyCFunction)NULL, METH_VARARGS},
    {"ygconfig_set_clone_node_func", (PyCFunction)NULL, METH_VARARGS},

    {NULL, NULL, 0, NULL},
};

static struct PyModuleDef poga_module_def = {
    PyModuleDef_HEAD_INIT, "poga", NULL, 0, poga_functions, 0, 0, 0, 0,
};

POGA_MODINIT_FUNC PyInit_libpoga_capi(void) {
    PyObject *m, *capi;

    // detect type ready
    if (PyType_Ready(&PogaYGNodeRef_Type) < 0) {
        return NULL;
    }

    m = PyModule_Create(&poga_module_def);
    if (m == NULL) {
        return NULL;
    }

    // if (init_error(m) < 0) {
    //     return NULL;
    // }

    // if (init_buffer_proxy() < 0) {
    //     return NULL;
    // }

    // if (init_enums(m) < 0) {
    //     return NULL;
    // }

    PyModule_AddStringConstant(
        m, "version",
        POGA_STRINGIFY(POGA_VERSION_MAJOR) "." POGA_STRINGIFY(
            POGA_VERSION_MINOR) "." POGA_STRINGIFY(POGA_VERSION_MICRO));

    PyModule_AddObject(m, "version_info", Py_BuildValue("(iii)", 0, 0, 0));

    /* Create a Capsule containing the CAPI pointer */
    // capi = PyCapsule_New((void*)(&CAPI), "poga.CAPI", 0);
    // if (capi != NULL) {
    //     PyModule_AddObject(m, "CAPI", capi);
    // }

    return m;
}

#ifdef __cplusplus
}
#endif
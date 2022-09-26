#include "private.h"
#include "types.h"

/* Python C API binding Implement */
static PyObject* YGNodeRef_new(PyTypeObject* type,
                               PyObject* args,
                               PyObject* kwds) {
    PyErr_SetString(PyExc_TypeError, "The xxx type cannot be instantiated");
    return NULL;
}

static void YGNodeRef_dealloc(PogaYGNodeRef* o) {
    if (o->node) {
        // YGNodeFree(o->node);
        o->node = NULL;
    }
    // Py_CLEAR(o->base);
    Py_TYPE(o)->tp_free(o);
}

static Py_hash_t YGNodeRef_hash(PyObject* self) {
    return POGA_Py_hash_t_FromVoidPtr(((PogaYGNodeRef*)self)->node);
}

static PyObject* YGNodeRef_richcompare(PyObject* self, PyObject* other, int op) {
    if (Py_TYPE(self) == Py_TYPE(other))
        return Poga_richcompare(((PogaYGNodeRef*)self)->node,
                                ((PogaYGNodeRef*)other)->node, op);
    else {
        Py_INCREF(Py_NotImplemented);
        return Py_NotImplemented;
    }
}

static PyMethodDef YGNodeRef_methods[] = {
    //     {"__enter__", (PyCFunction)surface_ctx_enter, METH_NOARGS},
    //     {"__exit__", (PyCFunction)surface_ctx_exit, METH_VARARGS},
    // {"get_context", (PyCFunction)NULL, METH_NOARGS},
    // {"reserved", (PyCFunction)NULL, METH_NOARGS},
    // {"print", (PyCFunction)NULL, METH_NOARGS},
    // {"get_has_new_layout", (PyCFunction)NULL, METH_NOARGS},
    // {"get_node_type", (PyCFunction)NULL, METH_NOARGS},
    // {"has_measure_func", (PyCFunction)NULL, METH_NOARGS},
    // {"measure", (PyCFunction)NULL, METH_VARARGS},
    // {"has_baseline_func", (PyCFunction)NULL, METH_NOARGS},
    // {"baseline", (PyCFunction)NULL, METH_VARARGS},
    // {"get_dirtied", (PyCFunction)NULL, METH_NOARGS},
    // {"get_style", (PyCFunction)NULL, METH_NOARGS},
    // {"get_layout", (PyCFunction)NULL, METH_NOARGS},
    // {"get_line_index", (PyCFunction)NULL, METH_NOARGS},
    // {"is_reference_baseline", (PyCFunction)NULL, METH_NOARGS},
    // {"get_owner", (PyCFunction)NULL, METH_NOARGS},
    // {"get_parent", (PyCFunction)NULL, METH_NOARGS},
    // {"get_children", (PyCFunction)NULL, METH_NOARGS},
    // {"get_child", (PyCFunction)NULL, METH_VARARGS},
    // {"get_config", (PyCFunction)NULL, METH_NOARGS},
    // {"is_dirty", (PyCFunction)NULL, METH_NOARGS},
    // {"get_resolved_dimensions", (PyCFunction)NULL, METH_VARARGS},
    // {"get_leading_position", (PyCFunction)NULL, METH_VARARGS},
    // {"is_leading_position_defined", (PyCFunction)NULL, METH_VARARGS},
    // {"is_trailing_pos_defined", (PyCFunction)NULL, METH_VARARGS},
    // {"get_trailing_position", (PyCFunction)NULL, METH_VARARGS},
    // {"get_leading_margin", (PyCFunction)NULL, METH_VARARGS},
    // {"get_trailing_margin", (PyCFunction)NULL, METH_VARARGS},
    // {"get_leading_border", (PyCFunction)NULL, METH_VARARGS},
    // {"get_trailing_border", (PyCFunction)NULL, METH_VARARGS},
    // {"get_leading_padding", (PyCFunction)NULL, METH_VARARGS},
    // {"get_trailing_padding", (PyCFunction)NULL, METH_VARARGS},
    // {"get_leading_padding_and_border", (PyCFunction)NULL, METH_VARARGS},
    // {"get_trailing_padding_and_border", (PyCFunction)NULL, METH_VARARGS},
    // {"get_margin_for_asix", (PyCFunction)NULL, METH_VARARGS},
    // // setter
    // {"set_context", (PyCFunction)NULL, METH_VARARGS},
    // {"set_print_func", (PyCFunction)NULL, METH_VARARGS},
    // {"set_has_new_layout", (PyCFunction)NULL, METH_VARARGS},
    // {"set_node_type", (PyCFunction)NULL, METH_VARARGS},
    // {"set_measure_func", (PyCFunction)NULL, METH_VARARGS},
    // {"set_baseline_func", (PyCFunction)NULL, METH_VARARGS},
    // {"set_dirtied_func", (PyCFunction)NULL, METH_VARARGS},
    // {"set_style", (PyCFunction)NULL, METH_VARARGS},
    // {"set_layout", (PyCFunction)NULL, METH_VARARGS},
    // {"set_line_index", (PyCFunction)NULL, METH_VARARGS},
    // {"set_is_reference_baseline", (PyCFunction)NULL, METH_VARARGS},
    // {"set_owner", (PyCFunction)NULL, METH_VARARGS},
    // {"set_children", (PyCFunction)NULL, METH_VARARGS},

    // // rvalue override for setChildren
    // {"set_dirty", (PyCFunction)NULL, METH_VARARGS},
    // {"set_layout_last_owner_direction", (PyCFunction)NULL, METH_VARARGS},
    // {"set_layout_computed_flex_basis", (PyCFunction)NULL, METH_VARARGS},
    // {"set_layout_computed_flex_basis_generation", (PyCFunction)NULL,
    //  METH_VARARGS},
    // {"set_layout_measured_dimension", (PyCFunction)NULL, METH_VARARGS},
    // {"set_layout_had_overflow", (PyCFunction)NULL, METH_VARARGS},
    // {"set_layout_dimension", (PyCFunction)NULL, METH_VARARGS},
    // {"set_layout_direction", (PyCFunction)NULL, METH_VARARGS},
    // {"set_layout_margin", (PyCFunction)NULL, METH_VARARGS},
    // {"set_layout_border", (PyCFunction)NULL, METH_VARARGS},
    // {"set_layout_padding", (PyCFunction)NULL, METH_VARARGS},
    // {"set_layout_position", (PyCFunction)NULL, METH_VARARGS},
    // {"set_position", (PyCFunction)NULL, METH_VARARGS},
    // {"set_layout_does_legacy_flag_affects_layout", (PyCFunction)NULL,
    //  METH_VARARGS},
    // {"set_layout_did_use_legacy_flag", (PyCFunction)NULL, METH_VARARGS},
    // {"mark_dirty_and_propogate_downwards", (PyCFunction)NULL, METH_VARARGS},

    // // Other methods
    // {"margin_leading_value", (PyCFunction)NULL, METH_VARARGS},
    // {"margin_trailing_value", (PyCFunction)NULL, METH_VARARGS},
    // {"resolve_flex_basis_ptr", (PyCFunction)NULL, METH_VARARGS},
    // {"resolve_dimension", (PyCFunction)NULL, METH_VARARGS},
    // {"resolve_direction", (PyCFunction)NULL, METH_VARARGS},
    // {"clear_children", (PyCFunction)NULL, METH_VARARGS},
    // {"replace_child", (PyCFunction)NULL, METH_VARARGS},
    // {"insert_child", (PyCFunction)NULL, METH_VARARGS},
    // {"remove_child", (PyCFunction)NULL, METH_VARARGS},

    // {"clone_children_if_needed", (PyCFunction)NULL, METH_VARARGS},
    // {"mark_dirty_and_propogate", (PyCFunction)NULL, METH_VARARGS},
    // {"resolve_flex_grow", (PyCFunction)NULL, METH_VARARGS},
    // {"resolve_flex_shrink", (PyCFunction)NULL, METH_VARARGS},
    // {"is_node_flexible", (PyCFunction)NULL, METH_VARARGS},
    // {"did_use_legacy_flag", (PyCFunction)NULL, METH_VARARGS},
    // {"is_layout_tree_equal_to_node", (PyCFunction)NULL, METH_VARARGS},
    // {"reset", (PyCFunction)NULL, METH_VARARGS},
    {NULL, NULL, 0, NULL},
};

/* Poga YGNodeRef Define */
PyTypeObject PogaYGNodeRef_Type = {
    PyVarObject_HEAD_INIT(NULL, 0) "poga.YGNodeRef", /* tp_name */
    sizeof(PogaYGNodeRef),                           /* tp_basicsize */
    0,                                               /* tp_itemsize */
    (destructor)YGNodeRef_dealloc,                   /* tp_dealloc */
    0,                                               /* tp_print */
    0,                                               /* tp_getattr */
    0,                                               /* tp_setattr */
    0,                                               /* tp_compare */
    0,                                               /* tp_repr */
    0,                                               /* tp_as_number */
    0,                                               /* tp_as_sequence */
    0,                                               /* tp_as_mapping */
    YGNodeRef_hash,                                  /* tp_hash */
    0,                                               /* tp_call */
    0,                                               /* tp_str */
    0,                                               /* tp_getattro */
    0,                                               /* tp_setattro */
    0,                                               /* tp_as_buffer */
    Py_TPFLAGS_DEFAULT | Py_TPFLAGS_BASETYPE,        /* tp_flags */
    0,                                               /* tp_doc */
    0,                                               /* tp_traverse */
    0,                                               /* tp_clear */
    YGNodeRef_richcompare,                           /* tp_richcompare */
    0,                                               /* tp_weaklistoffset */
    0,                                               /* tp_iter */
    0,                                               /* tp_iternext */
    YGNodeRef_methods,                               /* tp_methods */
    0,                                               /* tp_members */
    0,                                               /* tp_getset */
    0,                                               /* tp_base */
    0,                                               /* tp_dict */
    0,                                               /* tp_descr_get */
    0,                                               /* tp_descr_set */
    0,                                               /* tp_dictoffset */
    0,                                               /* tp_init */
    0,                                               /* tp_alloc */
    (newfunc)YGNodeRef_new,                          /* tp_new */
    0,                                               /* tp_free */
    0,                                               /* tp_is_gc */
    0,                                               /* tp_bases */
};

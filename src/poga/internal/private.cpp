#include "private.h"

PyObject* Poga_richcompare(void* a, void* b, int op) {
    PyObject* res;

    switch (op) {
        case Py_EQ:
            res = (a == b) ? Py_True : Py_False;
            break;
        case Py_NE:
            res = (a != b) ? Py_True : Py_False;
            break;
        case Py_LT:
            res = (a < b) ? Py_True : Py_False;
            break;
        case Py_LE:
            res = (a <= b) ? Py_True : Py_False;
            break;
        case Py_GT:
            res = (a > b) ? Py_True : Py_False;
            break;
        case Py_GE:
            res = (a >= b) ? Py_True : Py_False;
            break;
        default:
            res = Py_NotImplemented;
            break;
    }

    Py_INCREF(res);
    return res;
}
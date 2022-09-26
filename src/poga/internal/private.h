#ifndef _POGA_PRIVATE_H_
#define _POGA_PRIVATE_H_

#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include <Yoga.h>

#define POGA_Py_hash_t_FromVoidPtr(p) ((Py_hash_t)(Py_ssize_t)(p))
#define POGA_STRINGIFY(s) POGA_STRINGIFY_ARG(s)
#define POGA_STRINGIFY_ARG(s) #s

#define POGA_VERSION_MAJOR 1
#define POGA_VERSION_MINOR 2
#define POGA_VERSION_MICRO 3

#ifdef __GNUC__
#define POGA_MODINIT_FUNC \
    __attribute__((visibility("default"))) PyMODINIT_FUNC
#else
#define POGA_MODINIT_FUNC PyMODINIT_FUNC
#endif

int init_error(PyObject *module);
int init_buffer_proxy(void);
int init_enums(PyObject* module);

PyObject* Poga_richcompare(void* a, void* b, int op);


#endif

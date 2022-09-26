#ifndef _PYYOGA_YGNODE_H_
#define _PYYOGA_YGNODE_H_

#include <Python.h>
#include <Yoga.h>

// here define Poga object type
typedef struct {
    PyObject_HEAD YGNodeRef node;
} PogaYGNodeRef;

extern PyTypeObject PogaYGNodeRef_Type;
// extern PyTypeObject PogaYGConfigRef_Type;

#endif
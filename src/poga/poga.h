#ifndef _POGA_H_
#define _POGA_H_

#include <Python.h>
#include <Yoga.h>

#ifdef __cplusplus
extern "C" {
#endif

/* Define structure for C API */
typedef struct {
    /* (type object, constructor) pairs */
    PyTypeObject* YGNodeRef_Type;
} Poga_CAPI_t;

// Define the library export interface

#ifdef __cplusplus
}
#endif

#endif
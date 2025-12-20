#define NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION
#include <Python.h>
#include <numpy/arrayobject.h>
#include <cstdio>

PyObject* CppFunc(PyObject* self, PyObject* const* args, Py_ssize_t narg)
{
    puts(">> Entering C++ Layer.");

    // read input numpy array and scalar
    PyArrayObject* pyobjArr = (PyArrayObject*)PyArray_FROM_OTF(args[0], NPY_FLOAT64, NPY_ARRAY_C_CONTIGUOUS);
    double f64Filler = PyFloat_AsDouble(args[1]);

    // fill the array with the scalar
    double* pf64Ptr0 = (double*)PyArray_DATA(pyobjArr);
    for (int64_t i = 0; i < PyArray_Size((PyObject*)pyobjArr); ++i)
    {
        *(pf64Ptr0 + i) = f64Filler;
    }

    return (PyObject*)pyobjArr;
}

static PyMethodDef aMeth[] = 
{
    {"CppFunc", (PyCFunction)CppFunc, METH_FASTCALL, ""},
    {NULL, NULL, 0, NULL}        /* Sentinel */
};

static struct PyModuleDef sMod = 
{
    PyModuleDef_HEAD_INIT,
    "",   /* name of module */
    NULL,
    -1,
    aMeth
};

PyMODINIT_FUNC
PyInit_ext(void)
{
    import_array();
    return PyModule_Create(&sMod);
}
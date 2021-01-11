#include "include.h"

PyObject* some_function(PyObject* self, PyObject* args)
{
    __int64 input_value;
    if (!PyArg_ParseTuple(args, "L", &input_value))
    {
        goto error;
    }
    return PyLong_FromLongLong(input_value + 1);
error:
    return 0;
}

PyMethodDef SpamMethods[] =
{
    {"add_one", (PyCFunction)some_function, METH_VARARGS,0 },
    {0,0,0,0}
};


static struct PyModuleDef spammodule = {
    PyModuleDef_HEAD_INIT,
    "spam",   /* name of module */
    "Module documetation", /* module documentation, may be NULL */
    -1,       /* size of per-interpreter state of the module,
                 or -1 if the module keeps state in global variables. */
    SpamMethods
};

PyMODINIT_FUNC
PyInit_spam(void)
{
    return PyModule_Create(&spammodule);
}
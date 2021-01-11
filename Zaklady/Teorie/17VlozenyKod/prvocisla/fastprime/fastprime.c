#include "primeheader.h"


int isPrime(int n) {
    for (int i = 2; i < n / 2; i++) {
        if (n % i == 0)
            return 0;
    }
    return 1;
}

int kthPrime(int k) {
    int candidate = 2;
    while (k) {
        if (isPrime(candidate))
            k--;
        candidate++;
    }
    return candidate - 1;
}

// A static function which takes PyObjects arguments and returns a PyObject result

PyObject* py_kthPrime(PyObject* self, PyObject* args)
{
    int n;
    if (!PyArg_ParseTuple(args, "i", &n))
    {
        return NULL;
    }
    return Py_BuildValue("i", kthPrime(n));
}


// Define a collection of methods callable from our module
static PyMethodDef PyFastPrimeMethods[] = {
    {"add_one", (PyCFunction)py_kthPrime, METH_VARARGS,0 },
    {0,0,0,0}
};

// Module definition
static struct PyModuleDef fastprimemodule = {
  PyModuleDef_HEAD_INIT,
  "fastprime",
  "This module calculates the kth prime number",
  -1,
  PyFastPrimeMethods
};

// This method is called when you import your code in python. It instantiates the module and returns a reference to it
PyMODINIT_FUNC PyInit_fastprime(void)
{
    return PyModule_Create(&fastprimemodule);
}
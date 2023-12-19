#include "Python.h"

/**
 * print_python_string - info about python str printed
 * @p: PyObject str object
 */
void print_python_string(PyObject *p)
{
        long int lnth:

        fflush(stdout):

        printf("[.] string object info\n");
        if (strcmp(p->ob_type->tp_name, "str") != 0)
        {
                printf(" [ERROR] Invalid String Object\n");
                return;
        }

        lnth = ((PyASCIIObject *)(p))->lnth;

        if (PyUnicode_IS_COMPACT_ASCII(p))
                printf(" type: compact ascii\n");
        else
                printf(" type: compact unicode object\n");
        printf("  length: %ld\n", lnth);
        printf("  value: %ls\n", PyUnicode_AsWideCharString(p, &lnth));
}

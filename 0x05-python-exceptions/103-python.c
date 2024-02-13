#include <Python.h>
#include <stdio.h>
/**
 * print_python_float - Data of PyFloatObject given
 * @p: PyObject
 */
void print_python_float(PyObject *p)
{
	double v = 0;
	char *strn = NULL;

	fflush(stdout);
	printf("[.] float object info\n");

	if (!PyFloat_CheckExact(p))
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}
	v = ((PyFloatObject *)p)->ob_fval;
	strn = PyOS_double_to_string(v, 'r', 0, Py_DTSF_ADD_DOT_0, NULL);
	printf("  value: %s\n", strn);
}
/**
 * print_python_bytes - PyBytesObject data given
 * @p: PyObject
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t s = 0, a = 0;
	char *strn = NULL;

	fflush(stdout);
	printf("[.] bytes object info\n");
	if (!PyBytes_CheckExact(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	s = PyBytes_Size(p);
	printf("  size: %zd\n", s);
	strn = (assert(PyBytes_Check(p)), (((PyBytesObject *)(p))->ob_sval));
	printf("  trying string: %s\n", strn);
	printf("  first %zd bytes:", s < 10 ? s + 1 : 10);
	while (a < s + 1 && a < 10)
	{
		printf(" %02hhx", strn[a]);
		a++;
	}
	printf("\n");
}
/**
 * print_python_list - PyListObject data given
 * @p: PyObject
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t s = 0;
	PyObject *it;
	int a = 0;

	fflush(stdout);
	printf("[*] Python list info\n");
	if (PyList_CheckExact(p))
	{
		s = PyList_GET_SIZE(p);
		printf("[*] Size of the Python List = %zd\n", s);
		printf("[*] Allocated = %lu\n", ((PyListObject *)p)->allocated);
		while (a < s)
		{
			it = PyList_GET_ITEM(p, a);
			printf("Element %d: %s\n", a, it->ob_type->tp_name);
			if (PyBytes_Check(it))
				print_python_bytes(it);
			else if (PyFloat_Check(it))
				print_python_float(it);
			a++;
		}
	}
	else
		printf("  [ERROR] Invalid List Object\n");
}

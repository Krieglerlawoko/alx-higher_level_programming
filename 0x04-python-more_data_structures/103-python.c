#include <stdio.h>
#include <Python.h>

/**
 * print_python_bytes - Bytes info printd
 *
 * @p: Object
 * Return: return nothin
 */
void print_python_bytes(PyObject *p)
{
	char *strn;
	long int s, a, l;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	s = ((PyVarObject *)(p))->ob_size;
	strn = ((PyBytesObject *)p)->ob_sval;

	printf("  size: %ld\n", s);
	printf("  trying string: %s\n", strn);

	if (s >= 10)
		l = 10;
	else
		l = s + 1;

	printf("  first %ld bytes:", l);

	for (a = 0; a < l; a++)
		if (strn[a] >= 0)
			printf(" %02x", strn[a]);
		else
			printf(" %02x", 256 + strn[a]);

	printf("\n");
}

/**
 * print_python_list - list info printd
 *
 * @p: Object
 * Return: return nothin
 */
void print_python_list(PyObject *p)
{
	long int s, a;
	PyListObject *list;
	PyObject *obj;

	s = ((PyVarObject *)(p))->ob_size;
	list = (PyListObject *)p;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", s);
	printf("[*] Allocated = %ld\n", list->allocated);

	for (a = 0; a < s; a++)
	{
		obj = ((PyListObject *)p)->ob_item[a];
		printf("Element %ld: %s\n", a, ((obj)->ob_type)->tp_name);
		if (PyBytes_Check(obj))
			print_python_bytes(obj);
	}
}

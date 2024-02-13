#include <Python.h>
#include <object.h>
#include <listobject.h>

void print_python_list_info(PyObject *p)
{
	long int syz = PyList_Size(p);
	int a;
	PyListObject *obj = (PyListObject *)p;

	printf("[*] Size of the Python List = %li\n", syz);
	printf("[*] Allocated = %li\n", obj->allocated);
	for (a = 0; a < syz; a++)
		printf("Element %i: %s\n", a, Py_TYPE(obj->ob_item[a])->tp_name);
}

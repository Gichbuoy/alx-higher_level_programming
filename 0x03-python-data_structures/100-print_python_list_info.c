#include <Python.h>
#include <stdio.h>

/**
 * print_python_list_info - Prints basic info about Python lists
 * @p: PyObject list
 *
 * Return: nothing
 */
void print_python_list_info(PyObject *p)
{
	Py_ssize_t list_size, i;
	PyObject *item;

	if (!PyList_Check(p))
	{
		fprintf(stderr, "Expected a Python list\n");
		return;
	}

	list_size = PyList_Size(p);
	printf("[*] Size of the Python list = %zd\n", list_size);
	printf("[*] Allocated = %zd\n", ((PyListObject *)p)->allocated);

	for (i = 0; i < list_size; i++)
	{
		item = PyList_GetItem(p, i);
		printf("Element %zd: %s\n", i, Py_TYPE(item)->tp_name);
	}
}

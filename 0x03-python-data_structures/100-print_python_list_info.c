#include <listobject.h>
#include <object.h>

/**
 * print_python_list_info - function that prints basic info about Python lists
 * @p: pointer to info
 *
 * Return: nothing
 */
void print_python_list_info(PyObject *p)
{
	long int size = PyList_Size(p);
	int x;
	pyListObject *obj = (PyListObject *)p;

	printf("[*] Size of the Python List = %li\n", size);
	printf("[*] Allocated = %li\n", obj->allocated);

	for (x = 0; x < size; x++)
		printf("Element %x: %s\n", x, Py_TYPE(obj->ob_item[x])->tp_name);
}


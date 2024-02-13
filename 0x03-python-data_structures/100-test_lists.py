import ctypes

lib = ctypes.CDLL('./libPyList.so')
lib.print_python_list_info.argtypes = [ctypes.py_object]
a = ['hello', 'World']
lib.print_python_list_info(a)
del a[1]
lib.print_python_list_info(a)
a = l + [4, 5, 6.0, (9, 8), [9, 8, 1024], "Holberton"]
lib.print_python_list_info(a)
a = []
lib.print_python_list_info(a)
a.append(0)
lib.print_python_list_info(a)
a.append(1)
a.append(2)
a.append(3)
a.append(4)
lib.print_python_list_info(a)
a.pop()
lib.print_python_list_info(a)

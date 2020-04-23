#!/usr/bin/python3

matrx = [[0] * 4 for _ in range(5)]

for i in range(5):
    for j in range(3):
        matrx[i][j] = int(input("Введите matrx[%d][%d] элемент: " % (i, j)))

for i in range(5):
    for j in range(3):
        matrx[i][3] += matrx[i][j]

print("Полученная матрица:")
for line in matrx:
    print(line)


def count_and_show_variables_size(variables_list, include_varlist_size=False):
    def namestr(obj, namespace):
        return [name for name in namespace if namespace[name] is obj]

    def show_size(x, level=0, include_level_0=False):
        import sys
        # Если НЕ хотите учитывать размер списка переменных для оценки то:
        if include_level_0 is False:
            if level != 0:
                size_count = sys.getsizeof(x)
                print("\t" * level,
                      "Имя переменной = %s; тип = %s; размер = %d; содержимое = " % (namestr(x, globals()),
                                                                                     type(x), sys.getsizeof(x)),
                      x)
            else:
                size_count = 0
        # Иначе, если хотите учитывать размер списка переменных для оценки то:
        else:
            size_count = sys.getsizeof(x)
            print("\t" * level,
                  "Имя переменной = %s; тип = %s; размер = %d; содержимое = " % (namestr(x, globals()), type(x),
                                                                                 sys.getsizeof(x)), x)
        if hasattr(x, "__iter__") and not isinstance(x, str):
            if hasattr(x, "items"):
                for key, value in x.items():
                    size_count += show_size(key, level + 1)
                    size_count += show_size(value, level + 1)
            else:
                for item in x:
                    size_count += show_size(item, level + 1)
        return size_count

    size_of_border_line_ = 80
    print("=" * size_of_border_line_)
    print("Данные о переменных:")
    total_size = show_size(variables_list, include_level_0=include_varlist_size)
    print("=" * size_of_border_line_)
    print("Суммарный размер всех переменных из списка:", total_size)


count_and_show_variables_size([matrx])

"""

Введите matrx[0][0] элемент: 1
Введите matrx[0][1] элемент: 2
Введите matrx[0][2] элемент: 3
Введите matrx[1][0] элемент: 4
Введите matrx[1][1] элемент: 5
Введите matrx[1][2] элемент: 6
Введите matrx[2][0] элемент: 7
Введите matrx[2][1] элемент: 8
Введите matrx[2][2] элемент: 9
Введите matrx[3][0] элемент: 0
Введите matrx[3][1] элемент: 10
Введите matrx[3][2] элемент: 11
Введите matrx[4][0] элемент: 12
Введите matrx[4][1] элемент: 13
Введите matrx[4][2] элемент: 14
Полученная матрица:
[1, 2, 3, 6]
[4, 5, 6, 15]
[7, 8, 9, 24]
[0, 10, 11, 21]
[12, 13, 14, 39]
================================================================================
Данные о переменных:
	 Имя переменной = ['matrx']; тип = <class 'list'>; размер = 120; содержимое =  [[1, 2, 3, 6], [4, 5, 6, 15], [7, 8, 9, 24], [0, 10, 11, 21], [12, 13, 14, 39]]
		 Имя переменной = []; тип = <class 'list'>; размер = 88; содержимое =  [1, 2, 3, 6]
			 Имя переменной = []; тип = <class 'int'>; размер = 28; содержимое =  1
			 Имя переменной = ['j']; тип = <class 'int'>; размер = 28; содержимое =  2
			 Имя переменной = []; тип = <class 'int'>; размер = 28; содержимое =  3
			 Имя переменной = []; тип = <class 'int'>; размер = 28; содержимое =  6
		 Имя переменной = []; тип = <class 'list'>; размер = 88; содержимое =  [4, 5, 6, 15]
			 Имя переменной = ['i']; тип = <class 'int'>; размер = 28; содержимое =  4
			 Имя переменной = []; тип = <class 'int'>; размер = 28; содержимое =  5
			 Имя переменной = []; тип = <class 'int'>; размер = 28; содержимое =  6
			 Имя переменной = []; тип = <class 'int'>; размер = 28; содержимое =  15
		 Имя переменной = []; тип = <class 'list'>; размер = 88; содержимое =  [7, 8, 9, 24]
			 Имя переменной = []; тип = <class 'int'>; размер = 28; содержимое =  7
			 Имя переменной = []; тип = <class 'int'>; размер = 28; содержимое =  8
			 Имя переменной = []; тип = <class 'int'>; размер = 28; содержимое =  9
			 Имя переменной = []; тип = <class 'int'>; размер = 28; содержимое =  24
		 Имя переменной = []; тип = <class 'list'>; размер = 88; содержимое =  [0, 10, 11, 21]
			 Имя переменной = []; тип = <class 'int'>; размер = 24; содержимое =  0
			 Имя переменной = []; тип = <class 'int'>; размер = 28; содержимое =  10
			 Имя переменной = []; тип = <class 'int'>; размер = 28; содержимое =  11
			 Имя переменной = []; тип = <class 'int'>; размер = 28; содержимое =  21
		 Имя переменной = ['line']; тип = <class 'list'>; размер = 88; содержимое =  [12, 13, 14, 39]
			 Имя переменной = []; тип = <class 'int'>; размер = 28; содержимое =  12
			 Имя переменной = []; тип = <class 'int'>; размер = 28; содержимое =  13
			 Имя переменной = []; тип = <class 'int'>; размер = 28; содержимое =  14
			 Имя переменной = []; тип = <class 'int'>; размер = 28; содержимое =  39
================================================================================
Суммарный размер всех переменных из списка: 1116
"""
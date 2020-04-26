
"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами на
промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.
"""
import random
import time

random.seed(time.time())

m = int(input("Введите длину массива m = "))
array = [random.random() * 50 for i in range(m)]
print("Несортированный массив:", array, sep="\n\t")


def sort_merge(array):
    if len(array) > 1:
        center = len(array) // 2
        right = array[center:]
        left = array[:center]

        sort_merge(right)
        sort_merge(left)

        a, b, c = 0, 0, 0

        while a < len(left) and b < len(right):
            if left[a] < right[b]:
                array[c] = left[a]
                a += 1
            else:
                array[c] = right[b]
                b += 1
            c += 1

        while a < len(left):
            array[c] = left[a]
            a += 1
            c += 1

        while b < len(right):
            array[c] = right[b]
            b += 1
            c += 1


sort_merge(array)
print("Cортированный по убыванию массив:", array, sep="\n\t")
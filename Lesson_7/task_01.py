"""
1. Отсортировать по убыванию методом «пузырька» одномерный целочисленный массив, заданный случайными числами на
промежутке [-100; 100). Вывести на экран исходный и отсортированный массивы.
"""
import random
import time

random.seed(time.time())

m = int(input("Введите длину массива m = "))
array = [random.randint(-100, 99) for i in range(m)]
print("Несортированный массив:", array, sep="\n\t")


def sort_bubble_reversed(array):
    # n = len(array)
    for j in range(0, len(array) - 1):
        for i in range(0, len(array) - j - 1):
            if array[i] < array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
        # print(array)


sort_bubble_reversed(array)
print("Cортированный по убыванию массив:", array, sep="\n\t")
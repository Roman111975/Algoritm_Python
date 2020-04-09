"""
Посчитать четные и нечетные цифры введенного натурального числа. Например, если введено число 34560, то у него 3 четные
цифры (4, 6 и 0) и 2 нечетные (3 и 5).


https://drive.google.com/file/d/1xjBrrfKYbda1nsOBEOZljFV4SbtGIRxq/view?usp=sharing
ссылка на блок-схемы
"""

even = 0
odd = 0

a = int(input("Введите натуральное число a: "))

while a != 0:
    if a % 2 == 0:
        even += 1
    else:
        odd += 1
    a = a // 10

print("Четных цифр:", even)
print("Нечетных цифр:", odd)
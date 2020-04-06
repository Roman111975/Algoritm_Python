#!/usr/bin/python3

"""
Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).
"""


a = float(input('Введите число a: '))
b = float(input('Введите число b: '))
c = float(input('Введите число c: '))


if a > b:
    if a > c:
        if b > c:
            print(b)
        else:
            print(c)
    else:
        print(a)
else:
    if b > c:
        if a > c:
            print(a)
        else:
            print(c)
    else:
        print(b)
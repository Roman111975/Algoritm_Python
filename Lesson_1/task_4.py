#!/usr/bin/python3

"""
Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.
"""

a = int(input('Введите трехзначное число: '))

b = a // 100
c = a // 10 % 10
d = a % 10

sum_ = b + c + d
mul_ = b * c * d

print('Cумма цифр = %d; Произведение цифр = %d' % (sum_, mul_))
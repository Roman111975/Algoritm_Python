#!/usr/bin/python3

"""
Пользователь вводит номер буквы в алфавите. Определить, какая это буква.
"""


x = int(input('Введите номер буквы: '))

char_num = x + ord("a") - 1

print(chr(char_num))
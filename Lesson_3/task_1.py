"""
В диапазоне натуральных чисел от 2 до 99 определить, сколько
из них кратны каждому из чисел в диапазоне от 2 до 9.
"""

array = [i for i in range(2, 50)]
krat = [0] * 10

for val in array:
    for d in range(2, 10):
        if val % d == 0:
            krat[d] += 1

for d in range(2, 10):
    print("В диапазоне натуральных чисел [2;99] количество чисел кратных %d = %d" % (d, krat[d]))
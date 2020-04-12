"""
В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба являться минимальными), так и различаться.
"""

import random
import time

random.seed(time.time())

RANDRANGE_MIN_VAL = -50
RANDRANGE_MAX_VAL = 50

VAL_ARR_SIZE = 10

val_arr = [random.randint(RANDRANGE_MIN_VAL, RANDRANGE_MAX_VAL) for _ in range(VAL_ARR_SIZE)]
print("Массив случайных целых чисел:\n", val_arr)

min_val1 = RANDRANGE_MAX_VAL + 1
min_idx1 = 0

min_val2 = RANDRANGE_MAX_VAL + 1
min_idx2 = 0

for i in range(len(val_arr)):
    val = val_arr[i]
    if val < min_val1:
        min_val1 = val
        min_idx1 = i
    elif val == min_val1 or val < min_val2:
        min_val2 = val
        min_idx2 = i

print("Минимальное значение 1: %d; Индекс: %d" % (min_val1, min_idx1))
print("Минимальное значение 2: %d; Индекс: %d" % (min_val2, min_idx2))
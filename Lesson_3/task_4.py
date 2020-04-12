"""
В массиве найти максимальный отрицательный элемент.
Вывести на экран его значение и позицию в массиве.
Примечание к задаче: пожалуйста не путайте «минимальный»
и «максимальный отрицательный». Это два абсолютно разных значения.
"""

import random
import time

random.seed(time.time())

RANDRANGE_MIN_VAL = -50
RANDRANGE_MAX_VAL = 50

VAL_ARR_SIZE = 10

val_arr = [random.randint(RANDRANGE_MIN_VAL, RANDRANGE_MAX_VAL) for _ in range(VAL_ARR_SIZE)]
print("Массив случайных целых чисел:\n", val_arr)

max_need_val = RANDRANGE_MIN_VAL - 1
max_need_idx = 0

for i in range(len(val_arr)):
    if val_arr[i] < 0 and val_arr[i] > max_need_val:
        max_need_val = val_arr[i]
        max_need_idx = i

print("Максимальный отрицательный элемент:")
print("Значение: %d\nИндекс: %d" % (max_need_val, max_need_idx))

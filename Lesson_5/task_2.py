"""
2. Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как
массив, элементы которого это цифры числа.
Например, пользователь ввёл A2 и C4F.
Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’].
Произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
"""
from collections import deque

hex_to_dec = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "A": 10, "B": 11, "C": 12,
              "D": 13, "E": 14, "F": 15}

dec_to_hex = {v: k for k, v in hex_to_dec.items()}


def hex_sum(val1, val2, prev_to_mind="0"):
    val1_dec = hex_to_dec[val1]
    val2_dec = hex_to_dec[val2]
    sum_val = val1_dec + val2_dec + hex_to_dec[prev_to_mind]
    return dec_to_hex[sum_val % 16], dec_to_hex[sum_val // 16]


def hex_mul(val1, val2, prev_to_mind="0"):
    val1_dec = hex_to_dec[val1]
    val2_dec = hex_to_dec[val2]
    mul_val = val1_dec * val2_dec + hex_to_dec[prev_to_mind]
    return dec_to_hex[mul_val % 16], dec_to_hex[mul_val // 16]


def mul_1hex_to_list(list1, hex1):
    deq1 = deque(list1)
    res_deq = deque()

    deq1_len = len(deq1)
    to_mind = "0"
    for i in range(deq1_len):
        val1 = deq1.pop()
        res_tmp = hex_mul(val1, hex1, to_mind)
        to_mind = res_tmp[1]
        res_deq.appendleft(res_tmp[0])
    if to_mind != "0":
        res_deq.appendleft(to_mind)
    return res_deq


def hex_list_sum(list1, list2):
    deq1 = deque(list1)
    deq2 = deque(list2)
    res_deq = deque()

    maxlen = max(len(deq1), len(deq2))

    to_mind = "0"
    for i in range(maxlen):
        val1 = deq1.pop() if len(deq1) > 0 else "0"
        val2 = deq2.pop() if len(deq2) > 0 else "0"
        res_tmp = hex_sum(val1, val2, to_mind)
        to_mind = res_tmp[1]
        res_deq.appendleft(res_tmp[0])
    if to_mind != "0":
        res_deq.appendleft(to_mind)

    return res_deq


def hex_list_mul(list1, list2):
    deq1 = deque(list1)
    deq2 = deque(list2)
    res_deq = deque()

    while len(deq1) > 0:
        hex1 = deq1.pop()
        res_deq.append(mul_1hex_to_list(deq2, hex1))

    for i in range(len(list1)):
        res_deq[i].extend(["0"] * i)

    result = []
    while len(res_deq) > 0:
        result = hex_list_sum(result, res_deq.pop())

    return result


if __name__ == "__main__":
    a = [i for i in str(input("Введите HEX число a = ")).upper()]
    b = [i for i in str(input("Введите HEX число b = ")).upper()]

    print("a + b =", list(hex_list_sum(a, b)))

    print("a * b =", list(hex_list_mul(a, b)))
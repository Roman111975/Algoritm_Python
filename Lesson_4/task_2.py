"""
2. Написать два алгоритма нахождения i-го по счёту простого числа. Первый - использовать алгоритм решето Эратосфена.
Второй - без использования "решета". Проанализировать скорость и сложность алгоритмов.
"""
import cProfile
import math


def count_n_prime_number(n):
    if n <= 0:
        print("Wrong 'n'")
        return False

    found_count = 0
    n_prime_val = 0

    number = 2
    while True:
        break_flag = False
        for divider in range(2, number):
            if number % divider == 0:
                break_flag = True
                break
        if not break_flag:
            found_count += 1
            n_prime_val = number
        if found_count == n:
            break
        number += 1
    return n_prime_val


"""
Измерение при помощи timeit:
    python3.5 -m timeit -n 100 -s "import task_02" "task_02.count_n_prime_number(10)"
    100 loops, best of 3: 16.7 usec per loop

    python3.5 -m timeit -n 100 -s "import task_02" "task_02.count_n_prime_number(100)"
    100 loops, best of 3: 1.76 msec per loop

    python3.5 -m timeit -n 100 -s "import task_02" "task_02.count_n_prime_number(1000)"
    100 loops, best of 3: 287 msec per loop

Измерение при помощи cProfile:
    cProfile.run('count_n_prime_number(10)'); 1    0.000    0.000    0.000    0.000 task_02.py:12(count_n_prime_number)

    cProfile.run('count_n_prime_number(100)'); 1    0.002    0.002    0.002    0.002 task_02.py:12(count_n_prime_number)

    cProfile.run('count_n_prime_number(1000)'); 1    0.300    0.300    0.300    0.300 task_02.py:12(count_n_prime_number)

    cProfile.run('count_n_prime_number(10000)'); 1   41.580   41.580   41.580   41.580 task_02.py:12(count_n_prime_number)

"""


def find_n_prime_eratosthenes(n):
    """
    Для приблизительной оценки существует асимптотический закон распределения простых чисел. В отрезке от 1 до n таких
    чисел имеется порядка 'n / ln(n)'
    """

    """
    Для нахождения обратной зависимости, решим уравнение численно, методом дихотомии
    """

    # Оценка длины отрезка натуральных числе, вмещающего в себя n простых чисел:

    # Аппроксимация не работает маленьких значениях, поэтому первые два простых числа обрабатываются константно.
    if n < 1:
        return False
    elif n == 1:
        return 2
    elif n == 2:
        return 3

    a = 2
    b = n ** 2
    eps_y = 0.5
    eps_x = 0.5

    val = 100500

    while abs(val) > eps_y and b - a > eps_x:
        c = (a + b) / 2
        val = c / math.log(c) - n
        # print(c, val)
        if val < 0:
            a = c
        elif val > 0:
            b = c
        else:
            break

    c = int(c) + 2

    """
    Можно было обойтись без оценки длины необходимого отрезка, а использовать дополнительные выделения памяти при
    достижении конца отрезка натуральных чисел, но недостаточном количестве полученных простых чисел. Но такой способ 
    потенциально более затратный по памяти и/или времени.
    """

    # Решето Эратосфена, на отрезке длинны 'c':
    prime = [True for _ in range(c)]

    p = 2
    while p * p <= c:
        if prime[p]:
            for i in range(p * 2, c, p):
                prime[i] = False

        p += 1

    prime_only = [p for p in range(2, c) if prime[p]]

    return prime_only[n - 1]


"""
Измерение при помощи timeit:
    python3.5 -m timeit -n 100 -s "import task_02" "task_02.find_n_prime_eratosthenes(10)"
    100 loops, best of 3: 18 usec per loop

    python3.5 -m timeit -n 100 -s "import task_02" "task_02.find_n_prime_eratosthenes(100)"
    100 loops, best of 3: 83 usec per loop

    python3.5 -m timeit -n 100 -s "import task_02" "task_02.find_n_prime_eratosthenes(1000)"
    100 loops, best of 3: 1.27 msec per loop

    python3.5 -m timeit -n 100 -s "import task_02" "task_02.find_n_prime_eratosthenes(10000)"
    100 loops, best of 3: 18.2 msec per loop
Измерение при помощи cProfile:
    cProfile.run('find_n_prime_eratosthenes(10)'); 1    0.000    0.000    0.000    0.000 task_02.py:59(find_n_prime_eratosthenes)
    cProfile.run('find_n_prime_eratosthenes(100)'); 1    0.000    0.000    0.000    0.000 task_02.py:59(find_n_prime_eratosthenes)
    cProfile.run('find_n_prime_eratosthenes(1000)'); 1    0.001    0.001    0.001    0.001 task_02.py:59(find_n_prime_eratosthenes)
    cProfile.run('find_n_prime_eratosthenes(10000)'); 1    0.011    0.011    0.019    0.019 task_02.py:59(find_n_prime_eratosthenes)

    cProfile.run('find_n_prime_eratosthenes(100000)'); 1    0.221    0.221    0.383    0.383 task_02.py:59(find_n_prime_eratosthenes)

    cProfile.run('find_n_prime_eratosthenes(1000000)'):
       ncalls  tottime  percall  cumtime  percall filename:lineno(function)
            1    0.045    0.045    4.227    4.227 <string>:1(<module>)
            1    0.518    0.518    0.518    0.518 task_02.py:109(<listcomp>)
            1    0.653    0.653    0.653    0.653 task_02.py:119(<listcomp>)
            1    3.010    3.010    4.181    4.181 task_02.py:59(find_n_prime_eratosthenes)
           37    0.000    0.000    0.000    0.000 {built-in method builtins.abs}
            1    0.000    0.000    4.227    4.227 {built-in method builtins.exec}
           36    0.000    0.000    0.000    0.000 {built-in method math.log}
            1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
"""

if __name__ == "__main__":
    k = 100
    res_1 = count_n_prime_number(k)
    res_2 = find_n_prime_eratosthenes(k)
    print("%d-ое простое числое:\n\tПрямой подсчет: %d\n\tРешето Эратосфена: %d" % (k, res_1, res_2))
"""
1. Проанализировать скорость и сложность одного - трёх любых алгоритмов,
разработанных в рамках домашнего задания первых
 трех уроков.
"""

"""
ЗАДАЧА #7 из домашнего задания к УРОКУ #2:
Написать программу, доказывающую или проверяющую, что для множества натуральных чисел выполняется равенство:
1+2+...+n = n(n+1)/2, где n – любое натуральное число.
Решил замерить скорость полного цикла установления истинности равенства результата выражений, а так же отдельно левую и
правую части (в одном случае идет инкрементое наполнение, во втором случае подсчет значения по формуле, плюс добавил еще
реализацию при помощи рекурсии).
"""
import cProfile
import sys

sys.setrecursionlimit(150000)


def recursive_sum(n):
    if n == 0:
        return 0
    res = n + recursive_sum(n - 1)
    return res


"""
Измерение при помощи timeit:
    python3.5 -m timeit -n 100 -s "import task_01" "task_01.recursive_sum(100)"
    100 loops, best of 3: 10.5 usec per loop

    python3.5 -m timeit -n 100 -s "import task_01" "task_01.recursive_sum(1000)"
    100 loops, best of 3: 191 usec per loop

    python3.5 -m timeit -n 100 -s "import task_01" "task_01.recursive_sum(10000)"
    100 loops, best of 3: 3.34 msec per loop

    python3.5 -m timeit -n 100 -s "import task_01" "task_01.recursive_sum(27500)"
    100 loops, best of 3: 10.6 msec per loop
    (больше чем 27500 не лезет, при любом значении setrecursionlimit)
Измерение при помощи cProfile:
    cProfile.run('recursive_sum(100)'); 101/1    0.000    0.000    0.000    0.000 task_01.py:17(recursive_sum)

    cProfile.run('recursive_sum(1000)'); 1001/1    0.001    0.000    0.001    0.001 task_01.py:17(recursive_sum)

    cProfile.run('recursive_sum(10000)'); 10001/1    0.007    0.000    0.007    0.007 task_01.py:17(recursive_sum)

    cProfile.run('recursive_sum(27500)'); 27501/1    0.021    0.000    0.021    0.021 task_01.py:17(recursive_sum)
"""


def cycle_sum(n):
    res = 0
    for i in range(n + 1):
        res += i
    return res


"""
Измерение при помощи timeit:
    python3.5 -m timeit -n 100 -s "import task_01" "task_01.cycle_sum(100)"
    100 loops, best of 3: 3.49 usec per loop

    python3.5 -m timeit -n 100 -s "import task_01" "task_01.cycle_sum(1000)"
    100 loops, best of 3: 36.8 usec per loop

    python3.5 -m timeit -n 100 -s "import task_01" "task_01.cycle_sum(10000)"
    100 loops, best of 3: 387 usec per loop

    python3.5 -m timeit -n 100 -s "import task_01" "task_01.cycle_sum(1000000)"
    100 loops, best of 3: 42.4 msec per loop
Измерение при помощи cProfile:
    cProfile.run("cycle_sum(100)"); 1    0.000    0.000    0.000    0.000 task_01.py:51(cycle_sum)

    cProfile.run("cycle_sum(1000)"); 1    0.000    0.000    0.000    0.000 task_01.py:51(cycle_sum)

    cProfile.run("cycle_sum(10000)"); 1    0.000    0.000    0.000    0.000 task_01.py:51(cycle_sum)
    cProfile.run("cycle_sum(1000000)"); 1    0.047    0.047    0.047    0.047 task_01.py:51(cycle_sum)

    cProfile.run("cycle_sum(100000000)"); 1    4.428    4.428    4.428    4.428 task_01.py:51(cycle_sum)
"""


def func_sum(n):
    return n * (n + 1) // 2


"""
Измерение при помощи timeit:
    python3.5 -m timeit -n 100 -s "import task_01" "task_01.func_sum(100)"
    100 loops, best of 3: 0.175 usec per loop

    python3.5 -m timeit -n 100 -s "import task_01" "task_01.func_sum(1000)"
    100 loops, best of 3: 0.191 usec per loop

    python3.5 -m timeit -n 100 -s "import task_01" "task_01.func_sum(10000)"
    100 loops, best of 3: 0.179 usec per loop

    python3.5 -m timeit -n 100 -s "import task_01" "task_01.func_sum(1000000)"
    100 loops, best of 3: 0.185 usec per loop

    python3.5 -m timeit -n 100 -s "import task_01" "task_01.func_sum(10000000000000000000000000000000)"
    100 loops, best of 3: 0.291 usec per loop
Измерение при помощи cProfile:
    cProfile.run('func_sum(100)'); 1    0.000    0.000    0.000    0.000 task_01.py:85(func_sum)

    cProfile.run('func_sum(1000)'); 1    0.000    0.000    0.000    0.000 task_01.py:85(func_sum)

    cProfile.run('func_sum(10000)'); 1    0.000    0.000    0.000    0.000 task_01.py:85(func_sum)

    cProfile.run('func_sum(1000000)'); 1    0.000    0.000    0.000    0.000 task_01.py:85(func_sum)

    cProfile.run('func_sum(10000000000000000000000000000000)'); 1    0.000    0.000    0.000    0.000 task_01.py:85(func_sum)
"""


def check_they_are_true(n):
    return cycle_sum(n) == func_sum(n)


"""
Измерение при помощи timeit:
    python3.5 -m timeit -n 100 -s "import task_01" "task_01.check_they_are_true(100)"
    100 loops, best of 3: 3.63 usec per loop
    python3.5 -m timeit -n 100 -s "import task_01" "task_01.check_they_are_true(1000)"
    100 loops, best of 3: 37.6 usec per loop

    python3.5 -m timeit -n 100 -s "import task_01" "task_01.check_they_are_true(10000)"
    100 loops, best of 3: 395 usec per loop

    python3.5 -m timeit -n 100 -s "import task_01" "task_01.check_they_are_true(1000000)"
    100 loops, best of 3: 42.4 msec per loop

Измерение при помощи cProfile:
    cProfile.run('check_they_are_true(100)'); 
        1    0.000    0.000    0.000    0.000 task_01.py:120(check_they_are_true)
        1    0.000    0.000    0.000    0.000 task_01.py:51(cycle_sum)
        1    0.000    0.000    0.000    0.000 task_01.py:85(func_sum)

    cProfile.run('check_they_are_true(1000)'); 
        1    0.000    0.000    0.000    0.000 task_01.py:120(check_they_are_true)
        1    0.000    0.000    0.000    0.000 task_01.py:51(cycle_sum)
        1    0.000    0.000    0.000    0.000 task_01.py:85(func_sum)

    cProfile.run('check_they_are_true(10000)'); 
        1    0.000    0.000    0.000    0.000 task_01.py:120(check_they_are_true)
        1    0.000    0.000    0.000    0.000 task_01.py:51(cycle_sum)
        1    0.000    0.000    0.000    0.000 task_01.py:85(func_sum)

    cProfile.run('check_they_are_true(1000000)'); 
        1    0.000    0.000    0.047    0.047 task_01.py:120(check_they_are_true)
        1    0.047    0.047    0.047    0.047 task_01.py:51(cycle_sum)
        1    0.000    0.000    0.000    0.000 task_01.py:85(func_sum)

    cProfile.run('check_they_are_true(100000000)'); 
        1    0.000    0.000    4.585    4.585 task_01.py:120(check_they_are_true)
        1    4.584    4.584    4.584    4.584 task_01.py:51(cycle_sum)
        1    0.000    0.000    0.000    0.000 task_01.py:85(func_sum)
"""

"""
Вывод:
    Самую худшую производительность показала рекурсивная функция, кроме того, она имеет ограничение по глубине рекурсии,
    то есть не может посчитать результат для значения n превышающего порог этой глубины. Так же плохую 
    производительность показал способ инкреметного накопления суммы, так как время выполнения данной функции будет 
    линейно расти в зависимости от n. Лучшая же производительность у подсчета значения по формуле. Время её выполения
    константно и не зависит от n. 
"""

if __name__ == "__main__":
    for i in range(0, 10001, 500):
        print("При n=%d:" % i, check_they_are_true(i))
# 2 урок 3 задание. Реверс числа
from memory_profiler import memory_usage


def decor(f):
    def wrapper(*args):
        m1 = memory_usage()
        res = f(args[0])
        m2 = memory_usage()
        mem_diff = m2[0] - m1[0]
        return mem_diff

    return wrapper


@decor
def r_number(numb, n_str=''):
    n_str += str(numb % 10)
    return f'{str(n_str) if numb < 10 else str(n_str) + str(r_number(numb // 10))}'


@decor
def revers_ss(numb):
    if numb == 0:
        return ''
    return f'{str(numb % 10)}{revers_ss(numb // 10)}'


@decor
def revers_sl(numb):
    return str(numb)[::-1]


n = 23123123123120000000
print(f'Рекурсия 1: {r_number(n)}')
print(f'Рекурсия 2: {revers_ss(n)}')
print(f'Слайс: {revers_sl(n)}')

"""
Явно, использование срезов более эффективное и с точки зрения занимаемой памяти и с точки зрения времени 
Рекурсия 1: 0.0234375
Рекурсия 2: 0.01171875
Слайс: 0.0
"""

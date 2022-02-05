# 2 урок 4 задание, найти сумму ряда
from memory_profiler import profile


@profile
def row_rec_0(n_0):
    def row_rec(n):
        if n == 0:
            return 0
        else:
            return 1 + row_rec(n - 1) / -2
    print(f'Рекурсия: Сумма последовательности равна: {row_rec(n_0)}')



@profile
def row_for(n):
    el = 1
    am = 0
    for i in range(n):
        am += el
        el = -el / 2
    return print(f'Цикл: Сумма последовательности равна: {am}')



row_rec_0(100)
row_for(100)

"""
Обернули функцию с рекурсией в другую функцию и вызываем функцию верхнего уровня. Это
сделано для того чтобы получить замер только внешней функции.

для рекурсии требуется больше выделенной памяти так как в памяти хранится стек вызовов функций
"""
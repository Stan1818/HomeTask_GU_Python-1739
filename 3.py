from random import randint
from timeit import timeit
from statistics import median


def median_lst(lst):
    return median(lst[:])


m = 10
lst = [randint(0, 100) for i in range(2 * m + 1)]
print(timeit("median_lst(lst[:])", globals=globals(), number=100))

m = 100
lst = [randint(0, 100) for i in range(2 * m + 1)]
print(timeit("median_lst(lst[:])", globals=globals(), number=100))

m = 1000
lst = [randint(0, 100) for i in range(2 * m + 1)]
print(timeit("median_lst(lst[:])", globals=globals(), number=100))

"""
самый быстрый способ через функцию median
0.00011760008055716753
0.000726599944755435
0.01749599992763251
"""

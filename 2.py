from heapq import heappop, heappush
from random import randint
from timeit import timeit


def sort_heap(lst):
    lst_heap = []
    for i in lst:
        heappush(lst_heap, i)
    sort = []
    while lst_heap:
        sort.append(heappop(lst_heap))

    return sort

m=10
lst = [randint(0, 100) for i in range(2 * m + 1)]
print(timeit("sort_heap(lst[:])", globals=globals(), number=100))


m=100
lst = [randint(0, 100) for i in range(2 * m + 1)]
print(timeit("sort_heap(lst[:])", globals=globals(), number=100))

m=1000
lst = [randint(0, 100) for i in range(2 * m + 1)]
print(timeit("sort_heap(lst[:])", globals=globals(), number=100))

"""
Сложность алгоритма сортировки куча O(NlogN)

0.00039709999691694975
0.004654499934986234
0.06540169997606426

"""
from random import randint
from timeit import timeit


def without_sort(lst):
    temp = lst
    left_lst = []
    right_lst = []
    for i in range(len(temp)):
        for j in range(len(temp)):
            if temp[i] > temp[j]:
                left_lst.append(temp[j])
            if temp[i] < temp[j]:
                right_lst.append(temp[j])
            if temp[i] == temp[j] and i > j:
                left_lst.append(temp[j])
            if temp[i] == temp[j] and i < j:
                right_lst.append(temp[j])
        if len(left_lst) == len(right_lst):
            return temp[i]
        left_lst.clear()
        right_lst.clear()
m = 10
lst = [randint(0, 100) for i in range(2 * m + 1)]
print(timeit("without_sort(lst[:])", globals=globals(), number=100))

m = 100
lst = [randint(0, 100) for i in range(2 * m + 1)]
print(timeit("without_sort(lst[:])", globals=globals(), number=100))

m = 1000
lst = [randint(0, 100) for i in range(2 * m + 1)]
print(timeit("without_sort(lst[:])", globals=globals(), number=100))

"""
самый медленный способ без сортировки
0.010103499982506037
0.6671882000518963
80.04631820006762
"""

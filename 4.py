from random import randint
from timeit import timeit


def median_max_del(lst):
    temp_lst = lst
    for i in range(len(lst) // 2):
        temp_lst.remove(max(temp_lst))
    return max(temp_lst)


m = 10
lst = [randint(0, 100) for i in range(2 * m + 1)]
print(timeit("median_max_del(lst[:])", globals=globals(), number=100))

m = 100
lst = [randint(0, 100) for i in range(2 * m + 1)]
print(timeit("median_max_del(lst[:])", globals=globals(), number=100))

m = 1000
lst = [randint(0, 100) for i in range(2 * m + 1)]
print(timeit("median_max_del(lst[:])", globals=globals(), number=100))


"""
на втором месте удаление максимума
0.0008150000358000398
0.03560419997666031
2.7055447000311688
"""
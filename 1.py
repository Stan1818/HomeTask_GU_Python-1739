from timeit import timeit
from random import randint

lst = [randint(-100, 100) for i in range(20)]
print(f'Исходный массив: {lst}')

def sort_without_mark(lst):
    for i in range(len(lst)):
        for j in range(len(lst) - 1):
            if lst[j] < lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst


def sort_with_mark(lst):
    mark = True
    while mark:
        mark = False
        for i in range(len(lst) - 1):
            if lst[i] < lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
                mark = True
    return lst

print(sort_without_mark(lst))
print(sort_with_mark(lst))

t1 = timeit('sort_without_mark(lst[:])', globals=globals(), number=1000)
t2 = timeit('sort_with_mark(lst[:])',  globals=globals(), number=1000)
print(f'sort_without_mark: {t1}, sort_with_mark: {t2}')
print(f'Прирост скорости : {(t1 - t2) / t1 * 100} %')

"""
сортировка с маркером быстрее, так как массив может быть уже отсортирован, при таком условии мы сразу выходим из цикла
чем меньше массив, тем больше вероятность что он будет отсортирован

Исходный массив: [17, 63, 22, 97, -62, 24, 24, 51, -64, 31, 77, -95, -78, -11, -28, -54, -14, -97, 55, -21]
[97, 77, 63, 55, 51, 31, 24, 24, 22, 17, -11, -14, -21, -28, -54, -62, -64, -78, -95, -97]
[97, 77, 63, 55, 51, 31, 24, 24, 22, 17, -11, -14, -21, -28, -54, -62, -64, -78, -95, -97]
sort_without_mark: 0.028048900072462857, sort_with_mark: 0.0015075999544933438
Прирост скорости : 94.62510133873863 %
"""

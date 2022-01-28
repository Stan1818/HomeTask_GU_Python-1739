from timeit import timeit


# традиционный итератор
def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


# LC
def func_2(nums):
    return [i for i in range(len(nums)) if i % 2 == 0]



lst = [i for i in range(10000)]
print(f'традиционный итератор - {timeit("func_1(lst[:])", globals=globals(), number=100)}')
print(f'LC - {timeit("func_2(lst[:])", globals=globals(), number=100)}')


lst = [i for i in range(1000000)]
print(f'традиционный итератор - {timeit("func_1(lst[:])", globals=globals(), number=100)}')
print(f'LC - {timeit("func_2(lst[:])", globals=globals(), number=100)}')


"""
LC получается быстрее примерно на 20-30%

массив - 10000
традиционный итератор - 0.08283679999294691
LC - 0.051242099987575784

массив - 1000000
традиционный итератор - 10.975068299972918
LC - 7.1587388000043575
"""


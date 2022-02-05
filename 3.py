# 4 урок 1 задание, наполнение массива
from memory_profiler import profile
from random import randint


# традиционный итератор

@profile
def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


# LC
@profile
def func_2(nums):
    return [i for i in range(len(nums)) if i % 2 == 0]


lst = [randint(0, 100) for i in range(10000)]


func_1(lst)
func_2(lst)

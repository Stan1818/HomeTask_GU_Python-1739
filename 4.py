from random import randint
from memory_profiler import profile


array = [randint(0, 10) for i in range(100)]
@profile()
def func_1():
    new_array = []
    for el in array:
        count2 = array.count(el)
        new_array.append(count2)

    max_2 = max(new_array)
    elem = array[new_array.index(max_2)]
    return f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {max_2} раз(а)'

@profile
def func_2():
    return f'Чаще всего встречается число {max(array, key=array.count)}'

print(array)
print(func_1())
print(func_2())

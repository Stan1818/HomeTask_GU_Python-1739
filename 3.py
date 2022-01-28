from timeit import timeit


# рекурсия
def revers(enter_num, revers_num=0):
    if enter_num == 0:
        return
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        revers(enter_num, revers_num)


# цикл while
def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num


# срез
def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num


# цикл for
def revers_4(enter_num):
    enter_num = str(enter_num)
    revers_num = ''
    for i in range(len(enter_num) - 1, -1, -1):
        revers_num += enter_num[i]
    return revers_num


# функция reversed
def revers_5(enter_num):
    return ''.join(reversed(str(enter_num)))


n = 12345

print('Рекурсия: ', timeit(f'revers({n})', globals=globals(), number=1000000))
print('Цикл while: ', timeit(f'revers_2({n})', globals=globals(), number=1000000))
print('Срез: ', timeit(f'revers_3({n})', globals=globals(), number=1000000))
print('Цикл for: ', timeit(f'revers_4({n})', globals=globals(), number=1000000))
print('Функция reversed: ', timeit(f'revers_5({n})', globals=globals(), number=1000000))

"""
Срез самый быстрый
функция reversed на втором месте
странно что цикл while в некоторых запусках давал лучше результат чем цикл for (примерно одинаковое время)
Рекурсия самая медленная

Рекурсия:  1.245251599990297
Цикл while:  0.8302622999763116
Срез:  0.32406780001474544
Цикл for:  0.7995577999972738
Функция reversed:  0.4777057000028435

"""

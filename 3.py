dct = {'Ромашка': 1000, 'Тюльпан': 2000, 'Василек': 100, 'Лютик': 700, 'Одуван': 5000}


# O(n log n)
def ex1(sl):
    sl = sorted([(v, k) for (k, v) in sl.items()], reverse=True)[:3]  # O(n Log n)
    return print(sl)  # O(1)

# O(n^2)
def ex2(sl):
    lst = []
    for k, v in sl.items():
        lst.append([k, v])
    l = len(lst)
    for i in range(0, l):
        for j in range(0, l - i - 1):
            if (lst[j][1] < lst[j + 1][1]):
                tmp = lst[j]
                lst[j] = lst[j + 1]
                lst[j + 1] = tmp

    return print(lst[:3])

ex1(dct)
ex2(dct)

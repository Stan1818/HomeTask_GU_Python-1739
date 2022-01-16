lst = [100, -50, -3, 205, 10]

#O(n)
def min_n(lst):
    _min = lst[0]
    for i in range(len(lst)):
        if _min > lst[i]:
            _min = lst[i]
    return (_min)


#O(n^2)
def min_n_2(lst):
    _min = lst[0]
    for i in lst:
        for j in range(lst.index(i) + 1, len(lst) - 1, 1):
            if _min > lst[j]:
                _min = lst[j]
    return _min


print(min_n(lst))
print(min_n_2(lst))


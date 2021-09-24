src = [2, 2, 0, 2, 7, 23, 1, 99, 44, 44, 3, 2, 10, 7, 4, 11]
set1 = set()
set2 = set()
for i in src:
    if i not in set2:
        set1.add(i)
    else:
        set1.discard(i)
    set2.add(i)
result = [item for item in src if item in set1]
print(result)

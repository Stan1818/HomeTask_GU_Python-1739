src = [10000, 100001, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 34324]
result = [j for i, j in zip(src, src[1:]) if j > i]
print(result)

def count(n):
    res = (1, 0) if n % 2 == 0 else (0, 1)
    if n < 10:
        return res
    else:
        return tuple(map(sum, zip(count(n // 10), res)))

print(count(32230))
print(count(2222222))
print(count(111111111))

def ryad(n):
    if n == 0:
        return 0
    else:
        return 1 + ryad(n - 1) / -2

print(f'Сумма {ryad(10)}')
print(f'Сумма {ryad(0)}')

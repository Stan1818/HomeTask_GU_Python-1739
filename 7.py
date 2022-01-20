def equation(n):
    if n == 1:
        return n
    else:
        return equation(n - 1) + n


i = int(input("Введите число: "))
if equation(i) == i * (i + 1) / 2:
    print('Верно')

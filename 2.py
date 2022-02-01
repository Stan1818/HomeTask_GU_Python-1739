from collections import defaultdict

hex_dct = defaultdict(list)
n1 = input('Введите первое число: ')
n2 = input('Введите второе число: ')
lst = [n1, n2]

for i in range(2):
    hex_dct[lst[i]].extend(list(lst[i]))

add = hex(int(n1, 16) + int(n2, 16))[2:].upper()
mult = hex(int(n1, 16) * int(n2, 16))[2:].upper()
hex_dct[add].append(list(add))
hex_dct[mult].append(list(mult))
print(hex_dct)
print(f'Сумма равна {add}, произведение равно {mult}')

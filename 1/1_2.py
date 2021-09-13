list_3 = []
for i in range(1000):
    if i % 2 != 0:
        list_3.append(i ** 3)
i = 0
totalsum = 0
totalsum17 = 0
for i in range(len(list_3)):
    sumitem = 0
    temp = list_3[i]
    while list_3[i] != 0:
        sumitem = sumitem + list_3[i] % 10
        list_3[i] = list_3[i] // 10
    if sumitem % 7 == 0:
        list_3[i] = temp
        totalsum = totalsum + temp
    else:
        list_3[i] = temp
    list_3[i] = list_3[i] + 17
    sumitem17 = 0
    temp17 = list_3[i]
    while list_3[i] != 0:
        sumitem17 = sumitem17 + list_3[i] % 10
        list_3[i] = list_3[i] // 10
    if sumitem17 % 7 == 0:
        list_3[i] = temp17
        totalsum17 = totalsum17 + temp17

print('1-ая сумма:', totalsum)
print('2-ая сумма:', totalsum17)

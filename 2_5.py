list = [12.00, 12.6, 11.06, 233331.2342344, 32, 1234123, 231.4324324, 2312312.8, 12312.32321]
print('Исходный ИД списка: ', id(list))
print('Исходный список: ', list)
print('-' * 150)
list.sort()
for i in range(len(list)):
    list[i] = str(list[i])
    if list[i].isnumeric():
        list[i] = list[i] + ' руб 00 копеек'
    else:
        list[i] = "{:.2f}".format(float(list[i]))
        index = list[i].find('.')
        list[i] = list[i][0:index] + ' руб ' + list[i][index + 1:] + ' копеек'
str = ', '.join(list)
print('ИД списка после операций: ', id(list), '- сортировка по возрастанию')
print(str)
list_new = list[::-1]
print('-' * 150)
print('ИД нового списка: ', id(list_new), '- сортировка по убыванию')
str2 = ', '.join(list_new)
print(str2)
print('-' * 150)
print('ТОП 5 самых дорогих товаров')
maxstr = str2.split(', ')
lstmax = []
i = 0
for i in range(5):
    lstmax.append(maxstr[i])
lstmax.reverse()
for i in range(5):
    print(i + 1, ')', lstmax[i])

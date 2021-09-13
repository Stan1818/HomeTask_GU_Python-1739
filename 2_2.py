list = ['в', '5', 'часов', '07', 'минут', 'температура', 'воздуха', 'была', '-8', 'градусов']
print('ИД исходного листа: ', id(list))
print('Исходный список: ', list)
list_temp = []
for i in range(len(list)):
    if list[i].isnumeric() or list[i][-1].isnumeric():
        list_temp.append(list[i])

if len(list_temp[0]) == 1:
    hour = ['"', '0' + list_temp[0], '"']
    hour = [''.join(hour)]
else:
    hour = ['"', list_temp[0], '"']
    hour = [''.join(hour)]

if len(list_temp[1]) == 1:
    min = ['"', '0' + list_temp[1], '"']
    min = [''.join(min)]
else:
    min = ['"', list_temp[1], '"']
    min = [''.join(min)]

if len(list_temp[2]) == 2:
    grad = list_temp[2]
    grad = ['"', grad[0] + '0' + grad[1:], '"']
    grad = [''.join(grad)]
else:
    grad = ['"', list_temp[2], '"']
    grad = [''.join(grad)]

for item in list_temp:
    list.remove(item)

list.insert(1, hour[0])
list.insert(3, min[0])
list.insert(8, grad[0])
print('-' * 150)
print('ИД листа после операций: ', id(list))
print(' '.join(list))

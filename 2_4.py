list = ['инженер-конструктор игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
for i in range(len(list)):
    index = list[i].rfind(' ')
    list[i] = list[i][0:index + 1] + list[i][index + 1:].lower().title()
    print('Привет', list[i][index + 1:] + '!')
print(list)

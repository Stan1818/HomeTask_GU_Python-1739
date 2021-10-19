class OwnErr(Exception):
    def __init__(self, txt):
        self.txt = txt


class Check:
    def __init__(self):
        self.my_list = []

    def checking(self):
        global ext
        while True:
            try:
                num = (input('Введите число или числа через пробел: ')).split()
                for i in num:
                    self.my_list.append(int(i))
                ext = input('продолжить? y/n ')
                if ext == 'n':
                    print(f'Сформированный список: {self.my_list}')
                    break
            except ValueError:
                print('Ошибка. Введите числовой тип данных')

a = Check()
a.checking()

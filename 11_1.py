from datetime import date
import re

class Data:
    def __init__(self, data):
        self.data = data.split('-')

    @classmethod
    def type_int(cls, data):
        try:
            day, month, year = [int(i) for i in data.split('-')]
            return print(f"{day: 4} - > {type(day)}\n{month: 4} - > {type(month)}\n{year} - > {type(year)}")
        except ValueError:
            return print(f'Ошибка. Введите корректные данные')


def valid_data(data):
    global maindata
    try:
        maindata = re.sub(r'[./,\s|-]', '-', data)
        day, month, year = maindata.split('-')
        date(int(year), int(month), int(day))
        return print(f'{day}.{month}.{year} - корректная дата')
    except ValueError:
        return print(f'Ошибка,такой даты {maindata} нет. Введите корректную дату.')


Data.type_int('fd-02-2001')
Data.type_int('28-02-2001')
print('-=-' * 20)
valid_data('29-02-2001')
valid_data('28 02.2001')

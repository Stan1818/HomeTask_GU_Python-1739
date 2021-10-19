class Warehouse:
    dct_main = {}

    def add(self, equpment, equpment_name, quantity_eq):
        if equpment in self.dct_main.keys() and equpment_name in self.dct_main[equpment].keys():
            self.dct_main[equpment][equpment_name] = self.dct_main[equpment][equpment_name] + quantity_eq
            return self.dct_main

        elif equpment in self.dct_main.keys() and equpment_name not in self.dct_main[equpment].keys():
            dct_main_sub = {}
            dct_main_sub[equpment_name] = quantity_eq
            self.dct_main[equpment].update(dct_main_sub)
            return self.dct_main
        else:
            dct_main_sub = {}
            dct_main_sub[equpment_name] = quantity_eq
            self.dct_main[equpment] = dct_main_sub
            return self.dct_main

    def get_eq(self, division, type_eq, equpment_name, quantity_eq):
        if type_eq in self.dct_main.keys() and quantity_eq <= self.dct_main[type_eq][equpment_name]:
            self.dct_main[type_eq][equpment_name] = self.dct_main[type_eq][equpment_name] - quantity_eq
            print(f'{division} получило {quantity_eq} штуки оборудования {type_eq}')
            return self.dct_main
        else:
            return "Товар закончился!"


class Equpment:
    type_eq = ''

    def __init__(self, name, price):
        self.name = name
        self.count = price


class Scaner(Equpment):
    def __init__(self, name, price):
        super().__init__(name, price)
        self.type_eq = 'Сканер'


class Xerox(Equpment):
    def __init__(self, name, price):
        super().__init__(name, price)
        self.type_eq = 'Ксерокс'


class Printer(Equpment):
    def __init__(self, name, price):
        super().__init__(name, price)
        self.type_eq = 'Принтер'


def add_eq():
    global price
    dct_type = {1: Printer, 2: Scaner, 3: Xerox}
    u_select = int(input('Какой тип оборудования добавить на склад?\n'
                         '1 - Принтер\n2 - Сканер\n3 - Ксерокс\n1, 2, 3 '))
    name = input('Введите марку: ')

    try:
        price = int(input('Введите стоимость: '))
    except TypeError as err:
        print(f'Введите числовые данные {err}')

    equpment = dct_type[u_select](name, price)
    return equpment


def show_stock(dct_warehouse):
    print(f'Доступное оборудование на складе: \n', '*' * 30)
    for i in dct_warehouse:
        lst_stock = []
        for j, v in dct_warehouse[i].items():
            lst_stock.append(f'{j} - остаток: {v} шт.\n')
        print(f'{i}\n{"".join(lst_stock)}')


warehouse = Warehouse()
end = ''
while True:
    a = add_eq()
    quantity_eq = int(input(f'Какое количество оборудования {a.type_eq} {a.name} вы хотите добавить на склад?: '))
    warehouse.add(a.type_eq, a.name, quantity_eq)
    end = input('Для выхода нажмите q, для продолжения Enter: ')
    if end.lower() == 'q':
        break


def forward_eq():
    dct_type_eq = {1: 'Принтер', 2: 'Сканер', 3: 'Ксерокс'}
    lst_show = []
    u_select = int(input('Какое оборудование передать в другое подразделение?\n'
                         '1 - Принтер\n2 - Сканер\n3 - Ксерокс\n 1, 2, 3 '))
    if dct_type_eq[u_select] in warehouse.dct_main.keys():
        for k, v in warehouse.dct_main[dct_type_eq[u_select]].items():
            lst_show.append(f'{k}: {v} шт.\n')
        print(f'В наличии:\n{"".join(lst_show)}')
        return dct_type_eq[u_select]
    else:
        print('Оборудования нет на складе')


def forward_to():
    division = input('Введите подразделение куда передать технику: ')
    type_eq = forward_eq()
    if type_eq != None:
        equpment_name = input('Введите название оборудования: ')
        quantity_eq = int(input(f'Какое количество {equpment_name} передать в {division}: '))
        return warehouse.get_eq(division, type_eq, equpment_name, quantity_eq)


while True:
    show_stock(warehouse.dct_main)
    forward_to()
    end = input('Для выхода нажмите q, для продолжения Enter: ')
    if end == 'q':
        break

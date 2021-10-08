class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self._income = {}
        self.name = name
        self.surname = surname
        self.position = position
        self.wage = wage
        self.bonus = bonus
        self._income.setdefault('wage', wage)
        self._income.setdefault('bonus', bonus)


class Position(Worker):
    def get_full_name(self):
        print(f'Сотрудник: {self.name} {self.surname}')

    def get_income(self):
        ss = sum(self._income.values())
        print(f'Совокупный доход  - {ss:,.2f} рублей')


a = Position('Stan', 'Andreev', 'SEO', 1000000, 5555555)
a.get_full_name()
a.get_income()

a = Position('Ivan', 'Ivanov', 'Manager', 10000, 5555)
a.get_full_name()
a.get_income()

class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f'Началась отрисовка {self.title}')


class Pen(Stationery):
    def draw(self):
        print(f'Началась отрисовка {self.title} ручкой')


class Pencil(Stationery):
    def draw(self):
        print(f'Началась отрисовка {self.title} карандашем')


class Handle(Stationery):
    def draw(self):
        print(f'Началась отрисовка {self.title} маркером')


a = Stationery('круга')
a.draw()

b = Pen('прямоугольнка')
b.draw()

c = Pencil('треугольника')
c.draw()

d = Handle('квадрта')
d.draw()

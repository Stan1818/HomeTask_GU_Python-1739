class Road:
    massa = 25
    thickness = 5

    def __init__(self, _length, _width):
        self.len = _length
        self.wid = _width

    def result(self):
        road2 = self.len * self.wid
        s = self.len * self.wid * self.massa * self.thickness / 1000
        print(f'Для покрытия {road2:,} квадратных метров дороги потребуется {s:,.0f} тонн асфальта')


a = Road(20, 5000)
a.result()

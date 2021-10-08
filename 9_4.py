import random


class Car:
    def __init__(self, name, is_police):
        self.speed = random.randint(30, 120)
        self.color = random.choice(['красная', 'белая', 'черная', 'жёлтая', 'синия', 'ораньжевая'])
        self.name = name
        self.police = is_police

    def go(self):
        print(f'{self.color} машина {self.name} поехала со скоростью {self.speed} км/ч.')

    def stop(self):
        print(f'{self.color} машина {self.name} остановилась')

    def turn(self):
        self.lst = ['налево', 'направо']
        print(f'{self.color} машина {self.name} поехала {random.choice(self.lst)}.')

    def showspeed(self):
        print(f'Текущая скорость автомобиля {self.name} {self.speed} км/ч.')


class TownCar(Car):
    def showspeed(self):
        if self.speed > 60:
            print(f'aвтомобиль {self.name} превышает скорость на {self.speed - 60} км/ч.')


class WorkCar(Car):
    def showspeed(self):
        if self.speed > 40:
            print(f'aвтомобиль {self.name} превышает скорость на {self.speed - 40} км/ч.')


class SportCar(Car):
    def sportcar(self):
        self.speed = random.randint(180, 320)
        print(f'Спортивный автомобиль едет со скоросью {self.speed} км/ч')


class PoliceCar(Car):
    def policecar(self):
        if self.police:
            print('Машина полицейская и ей можно все!')


p = PoliceCar('БМВ', True)
p.policecar()

a = Car('Мерседес', False)
d = TownCar('Вольво', False)
d.turn()
d.go()
d.showspeed()
a2 = TownCar('Мазда', False)
a2.turn()
a2.go()
a2.showspeed()

a.turn()
a.go()
a.showspeed()

f = SportCar('Ферари', False)
f.sportcar()

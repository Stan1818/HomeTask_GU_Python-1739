from abc import ABC, abstractmethod


class Сlothing(ABC):
    def __init__(self, v):
        self.v = v

    @abstractmethod
    def summ(self):
        pass

    def __add__(self, other):
        return


class Coat(Сlothing):
    def summ(self):
        s1 = f'Пальто: {self.v / 6.5 + 0.5}'
        return self.v / 6.5 + 0.5


class Suit(Сlothing):
    def summ(self):
        s2 = f'Костюм: {2 * self.v + 0.3}'
        return 2 * self.v + 0.3


a = Coat(130)
print('Пальто: ', a.summ())

b = Suit(90)
print('Костюм: ', b.summ())
print('Сумма: ', a.summ() + b.summ())

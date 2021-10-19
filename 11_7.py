class ComplexNum:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        if self.y + other.y < 0:
            return f'Сумма комплексных чисел: {self.x + other.x}{self.y + other.y}i'
        else:
            return f'Сумма комплексных чисел: {self.x + other.x}+{self.y + other.y}i'

    def __mul__(self, other):
        if (self.x * other.y + (other.x * self.y)) < 0:
            return f'Произведение комплексных чисел: {self.x * other.x - (self.y * other.y)}{self.x * other.y + (other.x * self.y)}i'
        else:
            return f'Произведение комплексных чисел: {self.x * other.x - (self.y * other.y)}+{self.x * other.y + (other.x * self.y)}i'


z1 = ComplexNum(342, 121)
z2 = ComplexNum(340, -130)
print(z1 + z2)
print(z1 * z2)

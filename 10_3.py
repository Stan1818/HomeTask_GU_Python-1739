class Cell:
    def __init__(self, cell):
        self.cell = cell

    def __add__(self, other):
        return self.cell + other.cell

    def __sub__(self, other):
        return self.cell - other.cell

    def __mul__(self, other):
        return self.cell * other.cell

    def __truediv__(self, other):
        return self.cell / other.cell

    def __floordiv__(self, other):
        return self.cell // other.cell

    def __str__(self):
        return f'{self.cell}'

    def make_order(self, row):
        s = f'*' * self.cell
        ss = '\n'.join([s[i:i + row] for i in range(0, len(s), row)])
        return ss


cell1 = Cell(23)
cell2 = Cell(4)

print(cell1, cell2)
print('Сумма: ', cell1 + cell2)
print('Разность: ', cell1 - cell2)
print('Умножение: ', cell1 * cell2)
print('Деление: ', cell1 / cell2)
print('Целочисленное деление: ', cell1 // cell2)
print(cell1.make_order(5))

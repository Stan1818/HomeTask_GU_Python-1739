class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __add__(self, other):
        try:
            return Matrix([[self.matrix[i][j] + other.matrix[i][j] for j in range(len(self.matrix[0]))] for i in
                           range(len(self.matrix))])
        except (IndexError) as e:
            print(f'Разная размерность матриц: {e}')

    def __str__(self):
        matrix = '\n'.join([' '.join(map(str, i)) for i in self.matrix]) + '\n' + '*' * 20
        return matrix


matrix1 = Matrix([[1, 1, 32, 56], [33, 33, 43, 121], [123, 32, 434, 34], [213, 23, 67, 67]])
matrix2 = Matrix([[9, 9, 343, 434], [8, 8, 454, 238], [1, 1, 32, 56], [1, 1, 32, 56]])

print(matrix1)
print(matrix2)
print(matrix1 + matrix2)

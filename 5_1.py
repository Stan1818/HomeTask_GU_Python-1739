def gen():
    generator = (i for i in range(1, int(input('Введите число: ')) + 1, 2))
    yield generator


for n in gen():
    print(list(n))

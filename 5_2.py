def gen():
    generator = (i for i in range(1, int(input('Введите число: ')) + 1, 2))
    return generator


for i in gen():
    print(i)

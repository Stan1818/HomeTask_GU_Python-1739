class OwnErr(Exception):
    def __init__(self, txt):
        self.txt = txt


def division():
    try:
        n1 = int(input('Делимое: '))
        n2 = int(input('Делитель: '))
        if n2 == 0:
            raise OwnErr('Внимание, деление на 0')
    except ValueError:
        return 'Пожалуйста, введите число'
    except OwnErr as err:
        return err
    else:
        result = round(n1 / n2, 2)
        return f'Ответ: {result}'


print(division())

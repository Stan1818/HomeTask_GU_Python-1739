from random import randint


def get_num(n, i=10):
    number = int(input(f'Угадайте число от 0 до 100. У вас {i} попыток: '))
    if i == 1:
        print(f'Вы не справились. Загаданое число {n}')
        return
    if number == n:
        print(f'Вы угадали число {n} c {11-i} попытки')
        return
    elif number > n:
        print(f'Загаданное число меньше')
        get_num(n, i - 1)
    else:
        print(f'Загаданное число больше')
        get_num(n, i - 1)


num = randint(1, 100)
print(num)
get_num(num)

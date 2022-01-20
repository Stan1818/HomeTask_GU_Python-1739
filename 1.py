def calculyao():
    expr = input('Выберите арифмитическию операцию: +, -, *, /. Выберите 0 для завершения: ')

    if expr == '0':
        return
    else:
        a = int(input('Введите число А: '))
        b = int(input('Введите число В: '))

        if expr == '+':
            print(f'Ответ: {a + b}')

        if expr == '-':
            print(f'Ответ: {a - b}')

        if expr == '*':
            print(f'Ответ: {a * b}')

        if expr == '/':
            print(f'Ответ: {a / b}')
        calculyao()


calculyao()

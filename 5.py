def ancii(i, d1, d2):
    if d1 == d2:
        return '\n'
    else:
        if i % 10 == 0:
            print(f'{d1:3} - {chr(d1):3}')
        else:
            print(f'{d1:3} - {chr(d1):3}', end='')
        i = i + 1
        d1 = d1 + 1
        return ancii(i, d1, d2)


print(ancii(1, 32, 129))

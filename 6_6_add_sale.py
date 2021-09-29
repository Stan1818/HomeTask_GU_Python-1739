from sys import argv


with open('bakery.csv', 'a', encoding='utf-8') as f:
    name, data = argv
    f.write(f'{data}\n')

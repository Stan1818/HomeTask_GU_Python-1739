from sys import argv

lst = []
with open('bakery.csv', 'r', encoding='utf-8') as f:
    sales = f.readlines()
    for i in range(len(sales)):
        lst.append(sales[i].strip())
    lenght_argv = len(argv)
    if lenght_argv == 3:
        print(lst[int(argv[1]) - 1:int(argv[2])])
    elif lenght_argv == 2:
        print(lst[int(argv[1]) - 1:])
    elif lenght_argv == 1:
        print(lst)

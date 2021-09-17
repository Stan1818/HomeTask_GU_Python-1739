def thesaurus(*list_name):
    # dct = dict.fromkeys(list_name)
    dct = {}
    for i in range(len(list_name)):
        dct.setdefault(list_name[i][0], [])
    for x in dct:
        for i in range(len(list_name)):
            if list_name[i][0] == x:
                q = list_name[i]
                dct[x].append(q)
    print('*' * 25, 'Словарь без сортировки по ключу', '*' * 25)
    print(dct)
    sortdct = dict(sorted(dct.items(), key=lambda x: x[0]))
    print('*' * 25, 'Словарь c сортировкой по ключу', '*' * 25)
    print(sortdct)


thesaurus('Феликс', 'Стас', 'Саша', 'Сережа', 'Антон', "Иван", "Мария", "Петр", "Илья", "Ваня", 'Алекс', 'Макс')

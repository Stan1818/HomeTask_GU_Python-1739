from collections import Counter

s = "step by step!"
print(s)


def haffman(n):
    dct_c = Counter(n)
    lst = sorted([[el, el2] for el, el2 in dct_c.items()], key=lambda item: item[1])
    if len(lst) != 1:
        while len(lst) > 1:
            wight = lst[0][1] + lst[1][1]
            comb = {0: lst.pop(0)[0], 1: lst.pop(0)[0]}
            for i, el in enumerate(lst):
                if wight > el[1]:
                    continue
                else:
                    lst.insert(i, (comb, wight))
                    break
            else:
                lst.append((comb, wight))
    else:
        weight = lst[0][1]
        comb = {0: lst.pop(0)[0], 1: None}
        lst.append((comb, weight))
    print(lst)
    return lst[0][0]


dct_t = dict()


def haffman_code(tree, path=''):
    if not isinstance(tree, dict):
        dct_t[tree] = path
    else:
        haffman_code(tree[0], path=f'{path}0')
        haffman_code(tree[1], path=f'{path}1')


haffman_code(haffman(s))
ss = ''
for i in s:
    print(dct_t[i], end=' ')
    ss += dct_t[i] + ' '
print(dct_t)
print('____Зашифрованная строка____')
print(ss)


def decode_v1(de_str, lst):
    str_final = ''
    de_str = de_str.split(' ')
    for el in de_str:
        for el2, el3 in lst.items():
            if el == el3:
                str_final = str_final + el2
    return str_final


print('____Дешифрованная строка____')
print(decode_v1(ss, dct_t))

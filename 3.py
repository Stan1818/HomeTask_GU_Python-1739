def r_number(numb, n_str=''):
    n_str += str(numb % 10)
    return n_str if numb < 10 else n_str + r_number(numb // 10)

print(r_number(123))
print(r_number(1230))
print(r_number(12300))

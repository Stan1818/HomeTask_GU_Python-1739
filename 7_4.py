import os

root_dir = f'{os.getcwd()}\\some_data'
print(root_dir)
dct = {
    100: 0,
    1000: 0,
    10000: 0,
    100000: 0
}
file100 = 0
file1000 = 0
file10000 = 0
file100000 = 0
print(os.stat(root_dir + '\\abgdohc.bin').st_size)
for root, dirs, files in os.walk(root_dir):
    for file in files:
        ff = os.path.join(root_dir, file)
        if os.stat(ff).st_size < 100:
            file100 = file100 + 1
        elif os.stat(ff).st_size > 100 and os.stat(ff).st_size < 1000:
            file1000 = file1000 + 1
        elif os.stat(ff).st_size > 1000 and os.stat(ff).st_size < 10000:
            file10000 = file10000 + 1
        elif os.stat(ff).st_size > 10000 and os.stat(ff).st_size < 100000:
            file100000 = file100000 + 1
dct[100] = file100
dct[1000] = file1000
dct[10000] = file10000
dct[100000] = file100000
print(dct)

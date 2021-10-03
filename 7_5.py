import os
from collections import defaultdict
from os.path import relpath

import django

file100 = 0
file1000 = 0
file10000 = 0
file100000 = 0
lst100 = []
lst1000 = []
lst10000 = []
lst100000 = []
dct = {}
root_dir = django.__path__[0]
django_files = defaultdict(list)
for root, dirs, files in os.walk(root_dir):
    for file in files:
        ext = file.rsplit('.', maxsplit=1)[-1].lower()
        rel_path = relpath(os.path.join(root, file), root_dir)
        full_path = os.path.join(root, file)
        django_files[ext].append(rel_path)
        if os.stat(full_path).st_size < 100:
            if ext not in lst100:
                lst100.append(ext)
            file100 = file100 + 1
            dct[100] = (file100, lst100)
        elif os.stat(full_path).st_size > 100 and os.stat(full_path).st_size < 1000:
            if ext not in lst1000:
                lst1000.append(ext)
            file1000 = file1000 + 1
            dct[1000] = (file1000, lst1000)
        elif os.stat(full_path).st_size > 1000 and os.stat(full_path).st_size < 10000:
            if ext not in lst10000:
                lst10000.append(ext)
            file10000 = file10000 + 1
            dct[10000] = (file10000, lst10000)
        elif os.stat(full_path).st_size > 10000 and os.stat(full_path).st_size < 100000:
            if ext not in lst100000:
                lst100000.append(ext)
            file100000 = file100000 + 1
            dct[100000] = (file100000, lst100000)

    # print(f'{ext}: {len(files)}')
print(dct)

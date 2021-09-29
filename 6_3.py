from itertools import zip_longest
import json

user = []
hobby = []
with open('users.csv', 'r', encoding='utf-8') as f_user:
    for i in f_user:
        user.append(f_user.readline().strip().replace(',', ' '))

with open('hobby.csv', 'r', encoding='utf-8') as f_hobby:
    for i in f_hobby:
        hobby.append(f_hobby.readline().strip())

res_dict = {i: j if len(user) > len(hobby) else print(exit(1)) for i, j in zip_longest(user, hobby)}

with open('result.json', 'w', encoding='utf-8') as f_result:
    json.dump(res_dict, f_result)

with open('result.json', 'r', encoding='utf-8') as f_result:
    load_from_file = json.load(f_result)
print(load_from_file)

import os
import yaml


def create_file(name_file):
    with open(name_file, 'w', encoding='utf-8') as f:
        f.write('some text from Stan')


with open('config.yaml', 'r', encoding='utf-8') as f:
    tree = yaml.full_load(f)
result_list = []
for i in tree:
    for j in tree[i]:
        for k in range(len(tree[i][j])):
            if type(tree[i][j][k]) is not dict:
                result_list.append(f'{i} {j} {tree[i][j][k]}')
            if type(tree[i][j][k]) is dict:
                for n in tree[i][j][k]:
                    if type(tree[i][j][k][n]) is list:
                        for m in range(len(tree[i][j][k][n])):
                            if type(tree[i][j][k][n][m]) is dict:
                                for l in tree[i][j][k][n][m]:
                                    if type(tree[i][j][k][n][m][l]) is list:
                                        for s in range(len(tree[i][j][k][n][m][l])):
                                            result_list.append(f'{i} {j} {n} {l} {tree[i][j][k][n][m][l][s]}')

for ss in range(len(result_list)):
    result_list[ss] = os.path.join(os.getcwd(), result_list[ss].replace(' ', "\\"))
    if not os.path.exists(result_list[ss][:result_list[ss].rfind('\\') + 1]):
        os.makedirs(result_list[ss][:result_list[ss].rfind('\\') + 1])
for ff in range(len(result_list)):
    create_file(result_list[ff])

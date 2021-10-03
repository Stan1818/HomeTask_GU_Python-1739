import os

parrentdir = 'my_project'
tree = ['settings', 'mainapp', 'adminapp', 'authapp']

if not os.path.exists(parrentdir):
    os.mkdir(parrentdir)
else:
    exit(1)

basedir = os.path.join(os.getcwd(), parrentdir)

for i in range(len(tree)):
    newdir = os.path.join(basedir, tree[i])
    os.makedirs(newdir)

from os import path, walk, listdir
import shutil

project = 'my_project'
temp = 'templates'

try:
    for root, dirs, files in walk(project):
        if temp in dirs and root != project:
            for i in listdir(path.join(root, temp)):
                shutil.copytree(path.join(root, temp, i), path.join(project, temp, i))
except FileExistsError:
    print('Error')

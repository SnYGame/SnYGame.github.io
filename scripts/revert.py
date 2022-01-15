import sys
import os
import shutil

def copy(path):
    new_path = path.split(os.path.sep, maxsplit=1)[1]
    print(f'{path} -> {new_path}')
    shutil.copyfile(path, new_path)


for root, dirs, files in os.walk("orig"):
    for fl in files:
        copy(os.path.join(root, fl))

shutil.rmtree("orig")
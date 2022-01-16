import sys
import os
import shutil
import json
import re

temp_link_re = re.compile(r'\[([^\[]+)\]\(temp_remove\)')
version_num_re = re.compile(r'(?<!# )(?<!#)\bv?((\d+)\.\d+\.\d+[b-z]?)\b')

def process(path):
    new_path = copy(path)
    auto_link(new_path)

def copy(path):
    new_path = path.split(os.path.sep, maxsplit=1)[1]
    os.makedirs(os.path.dirname(new_path), exist_ok=True)
    shutil.copyfile(path, new_path)
    print(f'{path} -> {new_path}')
    return new_path

def auto_link(path):
    with open(path, 'r+') as f:
        content = f.read()

        for replace in config:
            link = replace['link']
            diff_link = f'{link}.md' != f'/{path}'.replace(os.path.sep, '/')

            for keyword in replace['keywords']:
                pattern = re.compile(f'^((?!title: )(?!# ).*?(?![^\\[]*\\]))\\b({keyword})\\b', re.M)
                if diff_link:
                    content = pattern.sub(f'\\1[\\2]({link})', content)
                else:
                    while pattern.search(content):
                        content = pattern.sub(f'\\1[\\2](temp_remove)', content)
        
        content = temp_link_re.sub(r'\1', content)
        content = version_num_re.sub(r'[\g<0>](/game/changelog/v\2.html#v\1)', content)
        f.seek(0)
        f.write(content)

with open('scripts/auto_link_config.txt') as f:
    config = json.loads(f.read())

for root, dirs, files in os.walk("orig"):
    for fl in files:
        process(os.path.join(root, fl))
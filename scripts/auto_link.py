import sys
import os
import shutil
import json
import re

temp_link_re = re.compile(r'\[([^\[]+)\]\(temp_remove\)')
version_num_re = re.compile(r'(?<!# )(?<!#)\bv?((\d+)\.\d+\.\d+[b-z]?)\b')

def process(path):
    print(path)
    save_orig(path)
    auto_link(path)

def save_orig(path):
    new_path = os.path.join('orig', path)
    os.makedirs(os.path.dirname(new_path), exist_ok=True)
    shutil.copyfile(path, new_path)

def auto_link(path):
    with open(path, 'r+') as f:
        content = f.read()

        for replace in config:
            link = replace['link']
            sub_string = f'\\1[\\2]({link})' if f'{link}.md' != f'/{path}'.replace(os.path.sep, '/') else f'\\1[\\2](temp_remove)'

            for keyword in replace['keywords']:
                pattern = re.compile(f'^((?!title: )(?!# ).*(?![^\\[]*\\]))\\b({keyword})\\b', re.M)
                while pattern.search(content):
                    content = pattern.sub(sub_string, content)
        
        content = temp_link_re.sub(r'\1', content)
        content = version_num_re.sub(r'[\g<0>](/game/changelog/v\2.html#v\1)', content)
        f.seek(0)
        f.write(content)

assert not os.path.isdir('orig')

with open('scripts/auto_link_config.txt') as f:
    config = json.loads(f.read())

print(config)

for root, dirs, files in os.walk(sys.argv[1]):
    for fl in files:
        process(os.path.join(root, fl))
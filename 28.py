# coding: utf-8
from modules import extract_British_from_json
import re

def remove_markup(str):
    str = re.sub(r'\'{2,5}', '', str)
    str = re.sub(r'\[{2}([^|\]]+\|)?(.+?)\]{2}', r'\2', str)
    str = re.sub(r'\[.*?\]', '', str)
    str = re.sub(r'<.*?>', '', str)
    str = re.sub(r'\{{2}.*?\|.*?\|(.*?)\}{2}', r'\1', str)
    return str

if __name__ == '__main__':
    map = {}
    lines = re.split('\n\||\n\}', extract_British_from_json())
    for line in lines:
        temp_line = re.search(r'(.*) = (.*)', line, re.S)
        if temp_line is not None:
            key = temp_line.group(1)
            value = temp_line.group(2)
            map[key] = remove_markup(value)
    for key, value in map.items():
        print(key, value)

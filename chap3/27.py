# coding: utf-8
import os, sys
sys.path.append(os.getcwd())

from modules import extract_British_from_json
import re

if __name__ == '__main__':
    map = {}
    lines = re.split('\n\||\n\}', extract_British_from_json())
    for line in lines:
        temp_line = re.search(r'(.*) = (.*)', line, re.S)
        if temp_line is not None:
            key = temp_line.group(1)
            value = temp_line.group(2)
            remove_emp_value = re.sub(r'\'{2,5}', '', value)
            remove_link_value = re.sub(r'\[{2}([^|\]]+\|)?(.+?)\]{2}', r'\2', remove_emp_value)
            map[key] = remove_link_value
    for key, value in map.items():
        print(key, value)

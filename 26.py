# coding: utf-8
from modules import extract_British_from_json
import re

if __name__ == '__main__':
    map = {}
    lines = re.split('\n\||\n\}', extract_British_from_json())
    for line in lines:
        temp_line = re.search('(.*) = (.*)', line, re.S)
        if temp_line is not None:
            key = temp_line.group(1)
            value = temp_line.group(2)
            remove_emp_val = re.sub('\'{2,5}', '', value)
            map[key] = remove_emp_val
    for key, value in map.items():
        print(key, value)

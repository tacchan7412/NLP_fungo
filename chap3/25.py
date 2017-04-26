# coding: utf-8
import os, sys
sys.path.append(os.getcwd())

from modules import extract_British_from_json
import re

if __name__ == '__main__':
    map = {}
    lines = re.split('\n\||\n\}', extract_British_from_json())
    for line in lines:
        temp_line = re.search('(.*) = (.*)', line, re.S)
        if temp_line is not None:
            map[temp_line.group(1)] = temp_line.group(2)
    for key, value in map.items():
        print(key, value)

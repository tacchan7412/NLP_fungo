# coding: utf-8
import os, sys
sys.path.append(os.getcwd())

from modules import extract_British_from_json
import re

if __name__ == '__main__':
    lines = extract_British_from_json().split("\n")
    for line in lines:
        section_line = re.search('^(=+)(.*?)(=+)', line)
        if section_line is not None:
            if section_line.group(1) != section_line.group(3):
                break
            print(section_line.group(2).strip(), len(section_line.group(1)) - 1)

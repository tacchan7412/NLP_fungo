# coding: utf-8
import os, sys
sys.path.append(os.getcwd())

from modules import extract_British_from_json
import re

if __name__ == '__main__':
    lines = extract_British_from_json().split("\n")
    for line in lines:
        if "Category" in line:
            print(re.search('^\[\[Category:(.*?)(\|.*)*\]\]', line).group(1))

# coding: utf-8
import os, sys
sys.path.append(os.getcwd())

from modules import extract_British_from_json

if __name__ == '__main__':
    lines = extract_British_from_json().split("\n")
    for line in lines:
        if "Category" in line:
            print(line)

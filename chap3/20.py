# coding: utf-8
import os, sys
sys.path.append(os.getcwd())

from modules import extract_British_from_json
import json

if __name__ == '__main__':
    print(extract_British_from_json())

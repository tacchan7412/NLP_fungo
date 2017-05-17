# coding: utf-8
import os, sys
sys.path.append(os.getcwd())

import re
if __name__ == '__main__':
    f = open('data/nlp.txt.xml', 'r')
    lines = f.readlines()
    for line in lines:
        if '<word>' in line and '</word>' in line:
            re_line = re.search('<word>(.+?)</word>', line)
            print(re_line.group(1))

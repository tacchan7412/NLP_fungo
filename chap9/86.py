# coding: utf-8
import os, sys
sys.path.append(os.getcwd())

import codecs

if __name__ == '__main__':
    f = codecs.open('data/85.txt')
    for line in f:
        if 'United_States' in line:
            print(line.split('\t')[0])
            print(line.split('\t')[1])
            break

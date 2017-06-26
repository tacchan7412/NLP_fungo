# coding: utf-8
import os, sys
sys.path.append(os.getcwd())

import codecs
import numpy as np

if __name__ == '__main__':
    f = codecs.open('data/questions-words.txt')
    f_out = codecs.open('data/91.txt', 'w')

    flag = False
    line = f.readline()
    while line:
        if line == ": family\n":
            flag = True
            line = f.readline()
        elif flag and ": " in line:
            break
        elif flag and line:
            f_out.write(line)
            line = f.readline()
        else:
            line = f.readline()
    f.close()
    f_out.close()

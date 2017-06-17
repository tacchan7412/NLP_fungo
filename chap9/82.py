# coding: utf-8
import os, sys
sys.path.append(os.getcwd())

import codecs, random
import numpy as np

if __name__ == '__main__':
    f = codecs.open('data/81.txt', 'r')
    lines = f.readlines()
    f.close()

    f_out = codecs.open('data/82.txt', 'w')
    for line in lines:
        words = line.split(' ')
        for i, word in enumerate(words):
            window_size = random.randint(1, 5)
            window_list = list(range(-1*window_size, window_size + 1))
            window_list = np.delete(window_list, window_size)
            for j in window_list:
                if 0 <= i+j < len(words):
                    f_out.write(word+'\t'+words[i+j]+'\n')
    f_out.close()

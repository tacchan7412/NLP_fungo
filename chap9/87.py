# coding: utf-8
import os, sys
sys.path.append(os.getcwd())

import codecs
import numpy as np

if __name__ == '__main__':
    f = codecs.open('data/85.txt')
    for line in f:
        vec = line.split('\t')
        if 'United_States' == vec[0]:
            united_states_vec = np.array([float(x) for x in vec[1].split()])
            print(vec[0])
        elif 'U.S' == vec[0]:
            us_vec = np.array([float(x) for x in vec[1].split()])
            print(vec[0])

    print(np.matmul(united_states_vec,us_vec.T)/(np.linalg.norm(united_states_vec)*np.linalg.norm(us_vec)))

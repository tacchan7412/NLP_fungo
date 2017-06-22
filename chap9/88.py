# coding: utf-8
import os, sys
sys.path.append(os.getcwd())

import codecs
import numpy as np

if __name__ == '__main__':
    england_vec = np.array([])
    f = codecs.open('data/85.txt')
    for line in f:
        vec = line.split('\t')
        if 'England' == vec[0]:
            england_vec = np.array([float(x) for x in vec[1].split()])
            break

    similarity_dict = {}
    for line in f:
        vec = line.split('\t')
        if 'England' == vec[0]:
            continue
        op_vec = np.array([float(x) for x in vec[1].split()])
        similarity_dict[vec[0]] = np.matmul(england_vec,op_vec.T)/(np.linalg.norm(england_vec)*np.linalg.norm(op_vec))

    for k, v in sorted(similarity_dict.items(), key=lambda x:x[1])[::-1][:10]:
        print(k,v)

    f.close()

# coding: utf-8
import os, sys
sys.path.append(os.getcwd())

import codecs
import numpy as np

if __name__ == '__main__':
    composed_vec = np.zeros(300)
    f = codecs.open('data/85.txt')
    for line in f:
        vec = line.split('\t')
        if "Spain" == vec[0] or "Athens" == vec[0]:
            composed_vec += np.array([float(x) for x in vec[1].split()])
        elif "Madrid" == vec[0]:
            composed_vec -= np.array([float(x) for x in vec[1].split()])
    f = codecs.open('data/85.txt')
    similarity_dict = {}
    for line in f:
        vec = line.split('\t')
        if 'Spain' == vec[0]:
            continue
        op_vec = np.array([float(x) for x in vec[1].split()])
        similarity_dict[vec[0]] = np.matmul(composed_vec,op_vec.T)/(np.linalg.norm(composed_vec)*np.linalg.norm(op_vec))

    for k, v in sorted(similarity_dict.items(), key=lambda x:x[1])[::-1][:10]:
        print(k,v)

    f.close()

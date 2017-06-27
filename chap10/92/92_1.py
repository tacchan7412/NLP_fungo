# coding: utf-8
import os, sys
sys.path.append(os.getcwd())

import codecs
import numpy as np

def calc_similarity(dic, vector):
    max_sim = -2
    max_name = ''
    for k, v in dic.items():
        if np.matmul(v,vector.T)/(np.linalg.norm(v)*np.linalg.norm(vector)) > max_sim:
            max_sim = np.matmul(v,vector.T)/(np.linalg.norm(v)*np.linalg.norm(vector))
            max_name = k

    return [max_name, max_sim]


if __name__ == '__main__':
    f_out = codecs.open('data/92_1.txt', 'w')
    f = codecs.open('data/91.txt')
    f_dict = codecs.open('data/85.txt')

    vec_dict = {}
    for line_dic in f_dict:
        vec = line_dic.split('\t')
        vec_dict[vec[0]] = np.array([float(x) for x in vec[1].split()])

    line = f.readline()
    while line:
        words = line[:-1].split()
        if words[0] not in vec_dict or words[1] not in vec_dict or words[2] not in vec_dict:
            line = f.readline()
            continue
        vector = vec_dict[words[1]] + vec_dict[words[2]] - vec_dict[words[0]]
        [word, similarity] = calc_similarity(vec_dict, vector)
        f_out.write(' '.join(words) + ' ' + word + ' ' + str(similarity) + '\n')
        line = f.readline()

    f.close()
    f_out.close()
    f_dict.close()

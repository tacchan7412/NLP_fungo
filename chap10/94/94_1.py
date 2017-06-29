# coding: utf-8
import os, sys
sys.path.append(os.getcwd())

import codecs
import csv
import numpy as np


if __name__ == '__main__':
    f_out = codecs.open('data/94_1.csv', 'w')
    f = codecs.open('data/combined.csv')
    f_dict = codecs.open('data/85.txt')

    vec_dict = {}
    for line_dic in f_dict:
        vec = line_dic.split('\t')
        vec_dict[vec[0]] = np.array([float(x) for x in vec[1].split()])

    reader = csv.reader(f)
    header = next(reader)

    writer = csv.writer(f_out, lineterminator='\n')
    for words in reader:
        if words[0] not in vec_dict or words[1] not in vec_dict:
            continue
        writer.writerow(words+[np.matmul(vec_dict[words[0]],vec_dict[words[1]].T)/(np.linalg.norm(vec_dict[words[0]])*np.linalg.norm(vec_dict[words[1]]))])

    f.close()
    f_out.close()
    f_dict.close()

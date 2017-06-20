# coding: utf-8
import os, sys
sys.path.append(os.getcwd())

import codecs
import numpy as np
from sklearn.decomposition import PCA
from sklearn.feature_extraction import DictVectorizer

if __name__ == '__main__':
    f_x = codecs.open('data/84_sort.txt')
    f_out = codecs.open('data/85.txt', 'w')

    t_dic = {}
    c_dic = {}
    for line in f_x:
        data = line[:-1].split('\t')
        c_dic[data[1]] = float(data[2])
        if data[0] in t_dic:
            t_dic[data[0]].update(c_dic)
        else:
            t_dic[data[0]] = c_dic
        c_dic = {}

    key_list = []
    value_list = []
    for key, val in t_dic.items():
        key_list.append(key)
        value_list.append(val)

    v = DictVectorizer()
    vectors=v.fit_transform(value_list).toarray()

    pca = PCA(n_components = 300)
    pca.fit(vectors)
    vectors_pca = pca.transform(vectors)

    for (key, vec) in zip(key_list, vectors_pca):
        f_out.write(key+'\t')
        for num in vec:
            f_out.write(str(num)+' ')
        f_out.write('\n')

    f_x.close()
    f_out.close()

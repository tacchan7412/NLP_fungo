# coding: utf-8
import os, sys
sys.path.append(os.getcwd())

import codecs
import numpy as np
from gensim.models import word2vec


if __name__ == '__main__':
    model_path = 'data/90.model'
    model = word2vec.Word2Vec.load(model_path)
    f = codecs.open('data/country_names.txt')

    for line in f:
        country = ''
        name = line[:-1].split(' ')
        if len(name) > 1:
            country = '_'.join(name)
        else:
            country = name[0]
        if country in model.wv:
            print(country)
            print(model.wv[country])
    f.close()

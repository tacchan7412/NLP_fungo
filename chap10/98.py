# coding: utf-8
import os, sys
sys.path.append(os.getcwd())

import codecs
import numpy as np
from gensim.models import word2vec
from scipy.cluster.hierarchy import dendrogram,ward
from matplotlib import pyplot as plt


if __name__ == '__main__':
    countries = []
    data = []

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
            countries.append(country)
            data.append(model.wv[country])
    f.close()

    pred = ward(data)
    dendrogram(pred, labels=countries)

    plt.show()

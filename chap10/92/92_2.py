# coding: utf-8
import os, sys
sys.path.append(os.getcwd())

import codecs
import numpy as np
from gensim.models import word2vec

if __name__ == '__main__':
    f_out = codecs.open('data/92_2.txt', 'w')
    model_path = 'data/90.model'
    model = word2vec.Word2Vec.load(model_path)
    f = codecs.open('data/91.txt')

    line = f.readline()
    while line:
        words = line[:-1].split()
        if words[0] not in model.wv or words[1] not in model.wv or words[2] not in model.wv:
            line = f.readline()
            continue
        [(word, similarity)] = model.most_similar(positive=[words[1], words[2]], negative=[words[0]], topn=1)
        f_out.write(' '.join(words) + ' ' + word + ' ' + str(similarity) + '\n')
        line = f.readline()

    f.close()
    f_out.close()

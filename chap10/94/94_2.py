# coding: utf-8
import os, sys
sys.path.append(os.getcwd())

import codecs
import csv
import numpy as np
from gensim.models import word2vec


if __name__ == '__main__':
    f_out = codecs.open('data/94_2.csv', 'w')
    f = codecs.open('data/combined.csv')
    model_path = 'data/90.model'
    model = word2vec.Word2Vec.load(model_path)

    reader = csv.reader(f)
    header = next(reader)

    writer = csv.writer(f_out, lineterminator='\n')
    for words in reader:
        if words[0] not in model.wv or words[1] not in model.wv:
            continue
        writer.writerow(words+[np.matmul(model.wv[words[0]],model.wv[words[1]].T)/(np.linalg.norm(model.wv[words[0]])*np.linalg.norm(model.wv[words[1]]))])

    f.close()
    f_out.close()

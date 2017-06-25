# coding: utf-8
import os, sys
sys.path.append(os.getcwd())

from gensim.models import word2vec

if __name__ == '__main__':
    model_path = 'data/90.model'
    model = word2vec.Word2Vec.load(model_path)

    print('86')
    print(model.wv['United_States'])

    print('87')
    print(model.wv.similarity('United_States', 'U.S'))

    print('88')
    print(model.most_similar(positive=['England'], negative=[], topn=10))

    print('89')
    print(model.most_similar(positive=['Spain', 'Athens'], negative=['Madrid'], topn=10))

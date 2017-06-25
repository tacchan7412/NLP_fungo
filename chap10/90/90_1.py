# coding: utf-8
import os, sys
sys.path.append(os.getcwd())

from gensim.models import word2vec

if __name__ == '__main__':
    sentences = word2vec.Text8Corpus('data/81.txt')
    model = word2vec.Word2Vec(sentences,
                              sg=1,
                              size=200,
                              min_count=10,
                              window=15,
                              hs=1,
                              negative=0)
    model.save('data/90.model')

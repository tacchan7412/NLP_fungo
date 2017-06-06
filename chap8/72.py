# coding: utf-8
import os, sys
sys.path.append(os.getcwd())

import codecs
from nltk import stem

f1 = codecs.open('data/stop_list.txt', 'r', 'latin_1')
stop_list = [x[:-1] for x in f1.readlines()]
f1.close()

def isinStopList(word):
    return word in stop_list

if __name__ == '__main__':
    stemmer = stem.PorterStemmer()
    f2 = codecs.open('data/sentiment.txt', 'r', 'latin_1')
    sentiments = f2.readlines()

    features_list = []
    for sentiment in sentiments:
        features = [sentiment.split()[0]]
        for word in sentiment.split()[1:]:
            word = stemmer.stem(word)
            if not isinStopList(word):
                features.append(word)
        features_list.append(features)

    print(features_list)

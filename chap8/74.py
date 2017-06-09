#!/usr/bin/env python

import codecs
import collections
import math
from nltk import stem


eta0 = 0.66
etan = 0.9999
guard = 0.0002

f1 = codecs.open('data/stop_list.txt', 'r', 'latin_1')
stop_list = [x[:-1] for x in f1.readlines()]
f1.close()

def isinStopList(word):
    return word in stop_list

def sigmoid(x):
  return 1.0 / (1.0 + math.exp(-x))

def update(W, features, label, eta):
  a = sum([W[x] for x in features])
  init_feature = 1
  predict = sigmoid(a)
  label = (label + 1) / 2

  for x in features:
    dif = eta * ( predict -label ) * init_feature
    if (W[x] - dif) > guard or (W[x] - dif) < (guard * -1):
      W[x] = W[x] - dif

if __name__ == "__main__":

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

    W = collections.defaultdict(float)
    for t, features in enumerate(features_list):
        update(W, features[1:], float(features[0]), eta0 * (etan**t))

    text = 'i had a great day while having a trip .'
    X_test = []
    for word in text.split():
        word = stemmer.stem(word)
        if not isinStopList(word):
            X_test.append(stemmer.stem(word))

    a = sum([W[x] for x in X_test])
    predict = sigmoid(a)
    predict = (predict * 2) - 1
    if predict > 0:
        predictlabel = "+1"
    elif predict < 0:
        predictlabel = "-1"
    else:
        predictlabel = "0"
    print("label",predictlabel,"\tpredict:",predict)

# coding: utf-8
import os, sys
sys.path.append(os.getcwd())

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
    Y_test = []
    X_test = []
    for sentiment in sentiments:
        Y_test.append(sentiment.split()[0])
        X = []
        features = [sentiment.split()[0]]
        for word in sentiment.split()[1:]:
            word = stemmer.stem(word)
            if not isinStopList(word):
                features.append(word)
                X.append(word)
        features_list.append(features)
        X_test.append(X)

    W = collections.defaultdict(float)
    for t, features in enumerate(features_list):
        update(W, features[1:], float(features[0]), eta0 * (etan**t))

    f_out = codecs.open('data/76.out','w')
    for (X, Y) in zip(X_test, Y_test):
        a = sum([W[x] for x in X])
        predict = sigmoid(a)
        if predict >= 0.5:
            f_out.write(Y+'\t'+'+1\t'+str(predict)+'\n')
        elif predict < 0.5:
            f_out.write(Y+'\t'+'-1\t'+str(1-predict)+'\n')
    f_out.close()

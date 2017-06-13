# coding: utf-8
import os, sys
sys.path.append(os.getcwd())

import codecs
import collections
import math
from nltk import stem
import numpy as np


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
    f2.close()

    sentiments = np.array(sentiments)
    np.random.shuffle(sentiments)
    splited_sentiments = np.array_split(sentiments, 5)

    scores = []
    precisions = []
    recalls = []
    f1_scores = []

    for i in range(5):
        Y_test = []
        X_test = []
        for sentiment in splited_sentiments[i]:
            Y_test.append(sentiment.split()[0])
            X = []
            for word in sentiment.split()[1:]:
                word = stemmer.stem(word)
                if not isinStopList(word):
                    X.append(word)
            X_test.append(X)

        splited_train_sentiments = splited_sentiments[:i]+splited_sentiments[i+1:]
        features_list = []
        for train_sentiments in splited_train_sentiments:
            for sentiment in train_sentiments:
                features = [sentiment.split()[0]]
                for word in sentiment.split()[1:]:
                    word = stemmer.stem(word)
                    if not isinStopList(word):
                        features.append(word)
                features_list.append(features)

        W = collections.defaultdict(float)
        for t, features in enumerate(features_list):
            update(W, features[1:], float(features[0]), eta0 * (etan**t))

        TP, FP, FN, TN = 0, 0, 0, 0
        for (X, Y) in zip(X_test, Y_test):
            a = sum([W[x] for x in X])
            predict = sigmoid(a)
            if predict >= 0.5 and Y == '+1':
                TP += 1
            elif predict < 0.5 and Y == '+1':
                FN += 1
            elif predict >= 0.5 and Y == '-1':
                FP += 1
            else:
                TN += 1

        score = (TP + TN) / len(Y_test)
        scores.append(score)
        precision = TP / (TP + FN)
        precisions.append(precision)
        recall = TP / (TP + FP)
        recalls.append(recall)
        f1_score = 2 / (1 / precision + 1 / recall)
        f1_scores.append(f1_score)

        print('trial',i+1,'-> \nscore:',score,'\nprecision:',precision,'\nrecall:',recall,'\nf1 score:',f1_score)

    print('mean-> \nscore:',np.mean(scores),'\nprecision:',np.mean(precisions),'\nrecall:',np.mean(recalls),'\nf1 score:',np.mean(f1_scores))

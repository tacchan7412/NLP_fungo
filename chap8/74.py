# coding: utf-8
import os, sys
sys.path.append(os.getcwd())

import codecs
from nltk import stem
from collections import OrderedDict
from sklearn.linear_model import LogisticRegression
import numpy as np

f1 = codecs.open('data/stop_list.txt', 'r', 'latin_1')
stop_list = [x[:-1] for x in f1.readlines()]
f1.close()

def isin_stopList(word):
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
            if not isin_stopList(word):
                features.append(word)
        features_list.append(features)

    feature_dict = {}
    for features in features_list:
        for feature in features[1:]:
            feature_dict[feature] = 0
    ordered_feature_dict = OrderedDict(sorted(feature_dict.items(), key=lambda t: t[0]))

    X = []
    Y = [x[0] for x in features_list]
    Y = list(map(lambda x: int((int(x)+1)/2), Y))
    for features in features_list:
        feature_dict_copy = ordered_feature_dict
        for feature in features[1:]:
            feature_dict_copy[feature] += 1
        X.append(list(feature_dict_copy.values()))

    clf = LogisticRegression()
    clf.fit(X,Y)

    texts = ['I hate you so much .', 'I drink a cup of coffee every morning .']
    X_test = []
    for text in texts:
        feature_dict_copy = ordered_feature_dict
        for word in text.split():
            feature_dict_copy[feature] += 1
        X_test.append(list(feature_dict_copy.values()))

    probas = clf.predict_proba(X_test)
    print(probas)
    for i, proba in enumerate(probas):
        label = ''
        prob = 0
        if np.array(proba).argmax() == 1:
            label = '+1'
            prob = proba[1]
        else:
            label = '-1'
            prob = proba[0]
        print(texts[i], label, prob)

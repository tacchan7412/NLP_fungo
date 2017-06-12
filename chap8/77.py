# coding: utf-8
import os, sys
sys.path.append(os.getcwd())

import codecs
import collections
import math
from nltk import stem

if __name__ == "__main__":
    f = codecs.open('data/76.out', 'r')
    lines = f.readlines()

    TP, FP, FN = 0, 0, 0
    for line in lines:
        [test_y, pred_y, _] = line.split('\t')
        if pred_y == '+1' and test_y == '+1':
            TP += 1
        elif pred_y == '-1' and test_y == '+1':
            FN += 1
        elif pred_y == '+1' and test_y == '-1':
            FP += 1

    precision = TP / (TP + FN)
    recall = TP / (TP + FP)
    f1_score = 2 / (1 / precision + 1 / recall)

    print("precision:",precision,"\nrecall:",recall,"\nf1 score:",f1_score)

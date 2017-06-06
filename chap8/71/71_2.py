# coding: utf-8
import os, sys
sys.path.append(os.getcwd())

import codecs
from collections import Counter

if __name__ == '__main__':
    f = codecs.open('data/sentiment.txt', 'r', 'latin_1')
    f_out = codecs.open('data/stop_list.txt', 'w', 'latin_1')
    sentiments = f.readlines()
    words = []
    for sentiment in sentiments:
        words += sentiment.split()
    c = Counter(words)
    for k, _ in c.most_common(100):
        if k != '+1' and k != '-1':
            f_out.write(k)
            f_out.write('\n')
    f.close()
    f_out.close()

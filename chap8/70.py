# coding: utf-8
import os, sys
sys.path.append(os.getcwd())

import random, codecs

if __name__ == '__main__':
    f_pos = codecs.open('data/rt-polaritydata/rt-polaritydata/rt-polarity.pos', 'r', 'latin_1')
    f_neg = codecs.open('data/rt-polaritydata/rt-polaritydata/rt-polarity.neg', 'r', 'latin_1')
    f_out = codecs.open('data/sentiment.txt', 'w', 'latin_1')

    pos = ['+1 '+x for x in f_pos]
    neg = ['-1 '+x for x in f_neg]
    lines = pos + neg

    random.shuffle(lines)
    f_out.writelines(lines)
    f_pos.close()
    f_neg.close()
    f_out.close()

    f = codecs.open('data/sentiment.txt', 'r', 'latin_1')
    sentiments = f.readlines()
    print('pos: '+str(len(list(filter(lambda x: x[:2]=='+1', sentiments)))))
    print('neg: '+str(len(list(filter(lambda x: x[:2]=='-1', sentiments)))))
    f.close()

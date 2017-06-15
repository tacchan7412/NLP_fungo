# coding: utf-8
import os, sys
sys.path.append(os.getcwd())

import codecs, re

if __name__ == '__main__':
    f = codecs.open('data/enwiki-20150112-400-r100-10576.txt', 'r')
    lines = f.readlines()
    f.close()
    f_out = codecs.open('data/80.txt', 'w')

    for line in lines:
        result = []
        words = line.split(' ')
        for word in words:
            word = re.sub(r'^[\.,!\?;:()\[\]\'"]*',r'',word)
            word = re.sub(r'[\.,!\?;:()\[\]\'"]*$',r'',word)
            if word:
                result.append(word)
        if result:
            f_out.writelines(' '.join(result))
    f_out.close()

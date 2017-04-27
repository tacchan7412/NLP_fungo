# coding: utf-8
import os, sys
sys.path.append(os.getcwd())

from modules import read_mecab
from functools import reduce

if __name__ == '__main__':
    result_set = set()
    morphologies = read_mecab()
    for sentence in morphologies:
        for i in range(len(sentence)-2):
            if sentence[i]['pos'] == '名詞' and sentence[i+1]['surface'] == 'の' and sentence[i+2]['pos'] == '名詞':
                result_set.add(sentence[i]['surface']+sentence[i+1]['surface']+sentence[i+2]['surface'])
    print(result_set)

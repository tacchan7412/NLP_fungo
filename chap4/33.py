# coding: utf-8
import os, sys
sys.path.append(os.getcwd())

from modules import read_mecab

if __name__ == '__main__':
    result_set = set()
    morphologies = read_mecab()
    for sentence in morphologies:
        for morphology in sentence:
            if morphology['pos1'] == 'サ変接続':
                result_set.add(morphology['surface'])
    print(result_set)

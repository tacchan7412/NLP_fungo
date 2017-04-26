# coding: utf-8
import os, sys
sys.path.append(os.getcwd())

from modules import read_mecab

if __name__ == '__main__':
    morphologies = read_mecab()
    for sentence in morphologies:
        for morphology in sentence:
            if morphology['pos'] == '動詞':
                print(morphology['surface'])

# coding: utf-8
import os, sys
sys.path.append(os.getcwd())

from collections import Counter
from modules import read_mecab

if __name__ == '__main__':
    counter = Counter([])
    morphologies = read_mecab()
    for sentence in morphologies:
        for morphology in sentence:
            counter.update([morphology["base"]])
    print(counter.most_common())
    for key, _ in counter.most_common():
        if len(key) > 1:
            print(key)

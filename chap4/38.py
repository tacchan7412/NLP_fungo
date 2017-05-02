# coding: utf-8
import os, sys
sys.path.append(os.getcwd())

from collections import Counter
import matplotlib.pyplot as plt
import numpy as np
from modules import read_mecab

if __name__ == '__main__':
    counter = Counter([])
    morphologies = read_mecab()
    for sentence in morphologies:
        for morphology in sentence:
            counter.update([morphology["base"]])

    cnt_list = []
    for _, val in counter.most_common():
        cnt_list.append(val)
    plt.hist(cnt_list, bins=100)
    plt.show()

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
    arr = np.array(counter.most_common(10))
    plt.bar(np.arange(10), arr[:,1].astype(np.int64), tick_label=arr[:,0])
    plt.show()

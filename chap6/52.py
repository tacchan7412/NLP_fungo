# coding: utf-8
import os, sys
sys.path.append(os.getcwd())

from nltk import stem
from modules import get_words_of_English

if __name__ == '__main__':
    words = get_words_of_English()
    stemmer = stem.PorterStemmer()
    words_split = words.split('\n')
    for word in words_split:
        if len(word) > 0:
            print(word + '\t' + stemmer.stem(word))
        else:
            print('\n')

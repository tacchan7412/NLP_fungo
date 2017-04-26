# coding: utf-8
import os, sys
sys.path.append(os.getcwd())

from modules import ngram

str = "I am an NLPer"

if __name__ == '__main__':
    str_for_word_list = str.split(" ")
    print(ngram(str_for_word_list, 2))

    str_for_letter = str.replace(" ", "", len(str))
    print(ngram(str_for_letter, 2))

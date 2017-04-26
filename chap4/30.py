# coding: utf-8
import os, sys
sys.path.append(os.getcwd())

from modules import read_mecab

if __name__ == '__main__':
    morphologies = read_mecab()
    # 動作確認用
    for i in range(10):
        print(morphologies[i])

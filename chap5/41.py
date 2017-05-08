# coding: utf-8
import os, sys
sys.path.append(os.getcwd())

from modules import read_cabocha_chunk

if __name__ == '__main__':
    sentences = read_cabocha_chunk()
    for chunk in sentences[2]:
        print(str(chunk))

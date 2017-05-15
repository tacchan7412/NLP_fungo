# coding: utf-8
import os, sys
sys.path.append(os.getcwd())

from modules import get_sentences_of_English

if __name__ == '__main__':
    sentences = get_sentences_of_English()
    _sentences = sentences.replace(".\n", ".\n\n", len(sentences))
    words = _sentences.replace(" ", "\n", len(_sentences))
    print(words)

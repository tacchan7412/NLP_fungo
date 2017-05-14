# coding: utf-8
import os, sys
sys.path.append(os.getcwd())

if __name__ == '__main__':
    f = open('data/nlp.txt', 'r')
    text = f.read()
    last_letters = [':', ';', '.', '?', '!']
    for i in range(len(text)-2):
        if text[i] in last_letters and text[i+1] == ' ' and text[i+2].isupper():
            text.join([text[:i]+'\n',text[i+1:]])
    print(text)
    f.close()

# coding: utf-8
import os, sys
sys.path.append(os.getcwd())

if __name__ == '__main__':
    f = open('data/nlp.txt', 'r')
    text = f.read()
    last_letters = [':', ';', '.', '?', '!']
    ans_text = text[0]
    for i in range(1, len(text)-1):
        if text[i-1] in last_letters and text[i] == ' ' and text[i+1].isupper():
            ans_text += '\n'
        else:
            ans_text += text[i]
    print(ans_text)
    f.close()

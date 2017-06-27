# coding: utf-8
import os, sys
sys.path.append(os.getcwd())

import codecs

if __name__ == '__main__':
    f1 = codecs.open('data/92_1.txt')

    line = f1.readline()
    all_cnt = 0
    cnt = 0
    while line:
        words = line[:-1].split()
        if words[3] == words[4]:
            cnt += 1
        all_cnt += 1
        line = f1.readline()
    print('85')
    print(cnt/all_cnt)

    f1.close()

    f2 = codecs.open('data/92_2.txt')

    line = f2.readline()
    all_cnt = 0
    cnt = 0
    while line:
        words = line[:-1].split()
        if words[3] == words[4]:
            cnt += 1
        all_cnt += 1
        line = f2.readline()
    print('91')
    print(cnt/all_cnt)

    f2.close()

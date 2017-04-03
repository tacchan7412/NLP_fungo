# coding: utf-8
import collections

if __name__ == '__main__':
    f = open('hightemp.txt', 'r')
    lines = f.readlines()
    col1 = []
    for line in lines:
        cols = line.split('\t')
        col1.append(cols[0])
    count_dict = collections.Counter(col1)
    for word, _ in count_dict.most_common():
        print(word)
    f.close()

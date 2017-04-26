# coding: utf-8
from operator import itemgetter

if __name__ == '__main__':
    f = open('data/hightemp.txt', 'r')
    lines = f.readlines()
    lines_list = []
    for line in lines:
        list = line.split('\t')
        lines_list.append(list)
    sorted_list = sorted(lines_list, key=itemgetter(2), reverse = True)
    print(sorted_list)
    f.close()

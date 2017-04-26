# coding: utf-8

import sys, math
args = sys.argv


if __name__ == '__main__':
    split_num = int(args[1])
    f = open('data/hightemp.txt', 'r')
    lines = f.readlines()
    step_num = math.ceil(len(lines)/split_num)
    for i in range(split_num):
        fout = open('data/out%d.txt'%i, 'w')
        if (i+1)*split_num > len(lines):
            str = ''.join(lines[i * step_num:len(lines)])
            fout.write(str)
        else:
            str = ''.join(lines[i * step_num:(i+1) * step_num])
            fout.write(str)
    f.close()

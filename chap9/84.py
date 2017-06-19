# coding: utf-8
import os, sys
sys.path.append(os.getcwd())

import codecs
import numpy as np

if __name__ == '__main__':
    f_tc10 = codecs.open('data/83_tc10.txt', 'r')
    f_t = codecs.open('data/83_t.txt', 'r')
    f_c = codecs.open('data/83_c.txt', 'r')
    f_N = codecs.open('data/83_N.txt', 'r')
    f_out = codecs.open('data/84.txt', 'w')

    N = int(f_N.readline().split(' ')[0])

    t_dict = {}
    for line in f_t:
        t = line[:-1].split(' ')
        t_dict[t[1]] = int(t[0])

    c_dict = {}
    for line in f_c:
        c = line[:-1].split(' ')
        c_dict[c[1]] = int(c[0])

    for line in f_tc10:
        tc_list = line[:-1].split(' ')
        tc = int(tc_list[0])
        [t, c] = tc_list[1].split('\t')
        X_tc = max(0, np.log(N) + np.log(tc) - np.log(t_dict[t]) - np.log(c_dict[c]))
        f_out.write('%s\t%s\t%f\n' %(t, c, X_tc))

    f_tc10.close()
    f_t.close()
    f_c.close()
    f_N.close()
    f_out.close()

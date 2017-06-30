# coding: utf-8
import os, sys
sys.path.append(os.getcwd())

import codecs
import csv
import numpy as np
from scipy.stats import rankdata


if __name__ == '__main__':
    f1 = codecs.open('data/94_1.csv')
    reader1 = csv.reader(f1)
    sim_human = np.array([float(row[2]) for row in reader1])
    f1.close()

    f1 = codecs.open('data/94_1.csv')
    reader1 = csv.reader(f1)
    sim1 = np.array([float(row[3]) for row in reader1])
    f1.close()

    rank_for_sim_human = rankdata(-sim_human, method='ordinal')
    rank_for_sim1 = rankdata(-sim1, method='ordinal')

    d1_sum = np.sum((rank_for_sim_human-rank_for_sim1)**2)
    r1 = 1 - 6*d1_sum/(len(sim_human)**3-len(sim_human))
    print('85')
    print('r: %f'%(r1))


    f2 = codecs.open('data/94_2.csv')
    reader2 = csv.reader(f2)
    sim_human = np.array([float(row[2]) for row in reader2])
    f2.close()

    f2 = codecs.open('data/94_2.csv')
    reader2 = csv.reader(f2)
    sim2 = np.array([float(row[3]) for row in reader2])
    f2.close()

    rank_for_sim_human = rankdata(-sim_human, method='ordinal')
    rank_for_sim2 = rankdata(-sim2, method='ordinal')

    d2_sum = np.sum((rank_for_sim_human-rank_for_sim2)**2)
    r2 = 1 - 6*d2_sum/(len(sim_human)**3-len(sim_human))

    print('90')
    print('r: %f'%(r2))

# coding: utf-8

if __name__ == '__main__':
    f = open('data/hightemp.txt', 'r')
    lines = f.readlines()
    fout1 = open('data/col1.txt', 'w')
    fout2 = open('data/col2.txt', 'w')
    for line in lines:
        cols = line.split('\t')
        fout1.write(cols[0] + '\n')
        fout2.write(cols[1] + '\n')
    f.close()
    fout1.close()
    fout2.close()

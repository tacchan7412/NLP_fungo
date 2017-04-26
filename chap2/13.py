# coding: utf-8

if __name__ == '__main__':
    f1 = open('data/col1.txt', 'r')
    f2 = open('data/col2.txt', 'r')
    fout = open('data/merged_cols.txt', 'w')
    col1 = f1.readlines()
    col2 = f2.readlines()
    for i in range(len(col1)):
        c1 = col1[i].replace('\n', '')
        c2 = col2[i].replace('\n', '')
        fout.write(c1 + '\t' + c2 + '\n' )
    f1.close()
    f2.close()
    fout.close()

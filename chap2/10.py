# coding: utf-8

if __name__ == '__main__':
    f = open('data/hightemp.txt', 'r')
    lines = f.readlines()
    print(len(lines))
    f.close()

# coding: utf-8

if __name__ == '__main__':
    f = open('data/hightemp.txt', 'r')
    str = f.read()
    str = str.replace("\t", " ", len(str))
    print(str)
    f.close()

# coding: utf-8

import sys
args = sys.argv


if __name__ == '__main__':
    f = open('hightemp.txt', 'r')
    lines = f.readlines()
    output = ''
    for i in range(int(args[1])):
        output += lines[i]
    print(output)
    f.close()

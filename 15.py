# coding: utf-8

import sys
args = sys.argv


if __name__ == '__main__':
    f = open('hightemp.txt', 'r')
    lines = f.readlines()
    output = ''
    for i in range(len(lines) - int(args[1]), len(lines)):
        output += lines[i]
    print(output)
    f.close()

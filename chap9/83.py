# coding: utf-8
import os, sys
sys.path.append(os.getcwd())


if __name__ == '__main__':
    print('unix command day!!')
    print('f(t,c):')
    print('cat data/82.txt | sort -k 1,2 | uniq -c | sort -nr > data/83_tc.txt')
    print('sed -i "" "s/^ *//g" "83_tc.txt"')
    print('f(t,*):')
    print('cut -f 1 data/82.txt | sort -k 1,2 | uniq -c | sort -nr > data/83_t.txt')
    print('sed -i "" "s/^ *//g" "83_t.txt"')
    print('f(t,*):')
    print('cut -f 2 data/82.txt | sort -k 1,2 | uniq -c | sort -nr > data/83_c.txt')
    print('sed -i "" "s/^ *//g" "83_c.txt"')
    print('N:')
    print('wc -l data/82.txt > 83_N.txt')

# coding: utf-8
import os, sys
sys.path.append(os.getcwd())

import codecs

f = codecs.open('data/stop_list.txt', 'r', 'latin_1')
stop_list = list(map(lambda x:x.replace('\n',''), f.readlines()))
f.close()

def isinStopList(word):
    return word in stop_list

# Test
if __name__ == '__main__':
    # 'hero' is not in stop_list
    print('hero: '+str(isinStopList('hero'))+' (must be False)')
    # 'is' is in stop_list
    print('is: '+str(isinStopList('is'))+' (must be True)')

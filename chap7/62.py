# coding: utf-8
import os, sys
sys.path.append(os.getcwd())

import redis

if __name__ == '__main__':
    r = redis.StrictRedis(host='localhost', port=6379, db=0)
    cnt = 0
    for key in r.scan_iter():
        if r.get(key).decode('utf-8') == 'Japan':
            cnt+=1
    print(cnt)

# coding: utf-8
import os, sys
sys.path.append(os.getcwd())

import redis

if __name__ == '__main__':
    r = redis.StrictRedis(host='localhost', port=6379, db=0)
    # 今回は name: 'Oasis'のレコードを確認
    print(r.get('Oasis').decode('utf-8'))

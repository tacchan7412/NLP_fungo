# coding: utf-8
import os, sys
sys.path.append(os.getcwd())

import json
import redis

if __name__ == '__main__':
    r = redis.StrictRedis(host='localhost', port=6379, db=0)
    f = open('data/artist.json', 'r')
    line = f.readline()
    while line:
        json_dict = json.loads(line)
        if 'name' in json_dict and 'area' in json_dict:
            r.set(json_dict['name'], json_dict['area'])
        line = f.readline()
    f.close()

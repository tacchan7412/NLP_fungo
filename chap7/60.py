# coding: utf-8
import os, sys
sys.path.append(os.getcwd())

import json
import redis

if __name__ == '__main__':
    r = redis.StrictRedis(host='localhost', port=6379, db=0)
    name_list = []
    f = open('data/artist.json', 'r')
    line = f.readline()
    while line:
        json_dict = json.loads(line)
        if 'name' in json_dict and 'area' in json_dict:
            r.set(json_dict['name'], json_dict['area'])
            name_list.append(json_dict['name'])
        line = f.readline()
    for i, name in enumerate(name_list):
        if i == 100:
            break
        print(r.get(name).decode('utf-8'))
    f.close()

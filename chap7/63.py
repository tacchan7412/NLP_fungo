# coding: utf-8
import os, sys
sys.path.append(os.getcwd())

import redis
import json
from ast import literal_eval

if __name__ == '__main__':
    r = redis.StrictRedis(host='localhost', port=6379, db=1)
    f = open('data/artist.json', 'r')
    line = f.readline()
    while line:
        json_dict = json.loads(line)
        if 'name' in json_dict and 'tags' in json_dict:
            r.set(json_dict['name'], json_dict['tags'])
        line = f.readline()
    f.close()

    # 確認用の名前
    key = 'Infester'
    tags = literal_eval(r.get(key).decode())

    for tag in tags:
        print("tag:",tag["value"],"\tcount:",tag["count"])

# coding: utf-8
import os, sys
sys.path.append(os.getcwd())

import pymongo
from pymongo import IndexModel
import json

if __name__ == '__main__':
    client = pymongo.MongoClient('localhost', 27017)
    db = client.MusicBrainz
    col = db.artist

    f = open('data/artist.json', 'r')
    line = f.readline()
    while line:
        json_dict = json.loads(line)
        col.insert_one(json_dict)
        line = f.readline()
    f.close()

    name_index = IndexModel([('name', pymongo.ASCENDING)])
    aliases_name_index = IndexModel([('aliases.name', pymongo.ASCENDING)])
    tags_value_index = IndexModel([('tags.value', pymongo.ASCENDING)])
    rating_value_index = IndexModel([('rating.value', pymongo.ASCENDING)])
    col.create_indexes([name_index, aliases_name_index, tags_value_index, rating_value_index])

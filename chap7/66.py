# coding: utf-8
import os, sys
sys.path.append(os.getcwd())

import pymongo
from pymongo import IndexModel

if __name__ == '__main__':
    client = pymongo.MongoClient('localhost', 27017)
    db = client.MusicBrainz
    col = db.artist

    print(col.find({'area': 'Japan'}).count())

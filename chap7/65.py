# coding: utf-8
import os, sys
sys.path.append(os.getcwd())

import pymongo

if __name__ == '__main__':
    client = pymongo.MongoClient('localhost', 27017)
    db = client.MusicBrainz
    col = db.artist

    # 本来は以下を出力
    Queen_list = list(col.find({'name': 'Queen'}))

    # 見やすくするために以下のように出力
    for el in Queen_list:
        print(el)

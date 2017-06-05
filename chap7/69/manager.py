# coding: utf-8
import os, sys
sys.path.append(os.getcwd())

import pymongo

def jsonid(x):
    x['_id']=str(x['_id'])
    return x

class Manager():
    def __init__(self):
        client = pymongo.MongoClient('localhost', 27017)
        db = client.MusicBrainz
        self.col = db.artist

    # 絞り込んでレーティングの高い順で返す
    def get_artists(self, name, aliase_name, tag, limit):
        search_dict = {}
        if name is not None:
            search_dict['name'] = name
        if aliase_name is not None:
            search_dict['aliases.name'] = aliase_name
        if tag is not None:
            search_dict['tags.value'] = tag
        if limit is not None:
            limit_num = int(limit)
        else:
            limit_num = 5

        artists_list = list(self.col.find(search_dict))
        artists_list = map(jsonid, artists_list)
        artists_list_with_rating = filter(lambda x: 'rating' in x, artists_list)
        sorted_artists_list_with_rating = sorted(artists_list_with_rating, key=lambda x:x['rating']['value'], reverse=True)

        return sorted_artists_list_with_rating[:min(limit_num, len(sorted_artists_list_with_rating))]

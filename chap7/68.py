# coding: utf-8
import os, sys
sys.path.append(os.getcwd())

import pymongo

if __name__ == '__main__':
    client = pymongo.MongoClient('localhost', 27017)
    db = client.MusicBrainz
    col = db.artist

    dance_list = list(col.find({'tags.value':'dance'}))
    dance_list_with_rating = filter(lambda x: 'rating' in x, dance_list)
    sorted_dance_list_with_rating = sorted(dance_list_with_rating, key=lambda x:x['rating']['count'], reverse=True)

    for el in sorted_dance_list_with_rating[:10]:
        print(el['name'], el['rating']['count'])

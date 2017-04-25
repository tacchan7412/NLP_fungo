# coding: utf-8
from modules import extract_British_from_json
import re
import requests

def remove_markup(str):
    str = re.sub(r'\'{2,5}', '', str)
    str = re.sub(r'\[{2}([^|\]]+\|)?(.+?)\]{2}', r'\2', str)
    str = re.sub(r'\[.*?\]', '', str)
    str = re.sub(r'<.*?>', '', str)
    str = re.sub(r'\{{2}.*?\|.*?\|(.*?)\}{2}', r'\1', str)
    return str

def search_json(json_file):
    json_dict = {}
    for k, v in json_file.items():
        if isinstance(v, list):
            for e in v:
                json_dict.update(search_json(e))
        elif isinstance(v, dict):
            json_dict.update(search_json(v))
        else:
            json_dict[k] = v
    return json_dict

if __name__ == '__main__':
    map = {}
    lines = re.split('\n\||\n\}', extract_British_from_json())
    for line in lines:
        temp_line = re.search(r'(.*) = (.*)', line, re.S)
        if temp_line is not None:
            key = temp_line.group(1)
            value = temp_line.group(2)
            map[key] = remove_markup(value)

    url = 'https://ja.wikipedia.org/w/api.php'
    payload = {
        'action': 'query',
        'titles': 'File:{}'.format(map['国旗画像']),
        'prop': 'imageinfo',
        'iiprop': 'url',
        'format': 'json'
    }
    json_file = requests.get(url, params=payload)
    json_dict = search_json(json_file.json())
    print(json_dict["url"])

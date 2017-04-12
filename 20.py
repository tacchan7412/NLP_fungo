# coding: utf-8
import json

if __name__ == '__main__':
    f = open('jawiki-country.json', 'r')
    line = f.readline()
    while line:
        json_dict = json.loads(line)
        if json_dict["title"] == "イギリス":
            print(json_dict["text"])
        line = f.readline()
    f.close()

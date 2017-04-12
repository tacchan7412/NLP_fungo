import json

def extract_British_from_json():
    f = open('jawiki-country.json', 'r')
    line = f.readline()
    while line:
        json_dict = json.loads(line)
        if json_dict["title"] == "イギリス":
            return json_dict["text"]
        line = f.readline()
    f.close()
    return ""

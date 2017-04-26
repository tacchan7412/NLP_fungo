import json

def ngram(sequence, n):
    output_list = []
    for i in range(len(sequence) - n + 1):
        output = sequence[i:i + n]
        output = "".join(output)
        output_list.append(output)
    return output_list

def extract_British_from_json():
    f = open('data/jawiki-country.json', 'r')
    line = f.readline()
    while line:
        json_dict = json.loads(line)
        if json_dict["title"] == "イギリス":
            return json_dict["text"]
        line = f.readline()
    f.close()
    return ""

def read_mecab():
    f = open('data/neko.txt.mecab', 'r')
    lines = f.readlines()
    morphologies = []
    sentence = []
    for line in lines:
        if 'EOS' in line:
            morphologies.append(sentence)
            sentence = []
        else:
            line_split = line.split('\t')
            surface = line_split[0]
            elems = line_split[1].split(',')
            sentence.append({
                'surface': surface,
                'base': elems[6],
                'pos': elems[0],
                'pos1': elems[1]
            })
    f.close()
    return morphologies

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

class Morph():
    def __init__(self, surface, base, pos, pos1):
        self.surface = surface
        self.base = base
        self.pos = pos
        self.pos1 = pos1

    def __str__(self):
        return 'surface: {}, base: {}, pos: {}, pos1: {}'.format(self.surface, self.base, self.pos, self.pos1)

class Chunk():
    def __init__(self, morphs, dst, srcs):
        self.morphs = morphs
        self.dst = int(dst)
        self.srcs = int(srcs)

    def __str__(self):
        return 'dst: {}, srcs: {}, morphs: {}'.format(self.dst, self.srcs, ' | '.join([str(morph) for morph in self.morphs]))

def read_cabocha_chunk():
    f = open('data/neko.txt.cabocha', 'r')
    lines = f.readlines()
    sentences = []
    chunk = None
    sentence = []
    for line in lines:
        if 'EOS' in line:
            if chunk is not None:
                sentence.append(chunk)
            chunk = None
            sentences.append(sentence)
            sentence = []
        elif '* ' in line:
            if chunk is not None:
                sentence.append(chunk)
                chunk = None
            line_split = line.split()
            chunk = Chunk([], line_split[2].rstrip('D'), line_split[1])
        else:
            line_split = line.split('\t')
            surface = line_split[0]
            elems = line_split[1].split(',')
            morph = Morph(surface, elems[6], elems[0], elems[1])
            chunk.morphs.append(morph)
    f.close()
    return sentences

def get_sentences_of_English():
    f = open('data/nlp.txt', 'r')
    text = f.read()
    last_letters = [':', ';', '.', '?', '!']
    ans_text = text[0]
    for i in range(1, len(text)-1):
        if text[i-1] in last_letters and text[i] == ' ' and text[i+1].isupper():
            ans_text += '\n'
        else:
            ans_text += text[i]
    f.close()
    return ans_text

def get_words_of_English():
    sentences = get_sentences_of_English()
    _sentences = sentences.replace(".\n", ".\n\n", len(sentences))
    words = _sentences.replace(" ", "\n", len(_sentences))
    return words

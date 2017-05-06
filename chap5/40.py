# coding: utf-8
import os, sys
sys.path.append(os.getcwd())

class Morph():
    def __init__(self, surface, base, pos, pos1):
        self.surface = surface
        self.base = base
        self.pos = pos
        self.pos1 = pos1

def read_cabocha_morph():
    f = open('data/neko.txt.cabocha', 'r')
    lines = f.readlines()
    morphologies = []
    sentence = []
    for line in lines:
        if 'EOS' in line:
            morphologies.append(sentence)
            sentence = []
        elif '* ' in line:
            continue
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

if __name__ == '__main__':
    morphologies = read_cabocha_morph()
    print(morphologies[2])

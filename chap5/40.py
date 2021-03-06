# coding: utf-8
import os, sys
sys.path.append(os.getcwd())

class Morph():
    def __init__(self, surface, base, pos, pos1):
        self.surface = surface
        self.base = base
        self.pos = pos
        self.pos1 = pos1

    def __str__(self):
        return 'surface: {}, base: {}, pos: {}, pos1: {}'.format(self.surface, self.base, self.pos, self.pos1)

def read_cabocha_morph():
    f = open('data/neko.txt.cabocha', 'r')
    lines = f.readlines()
    sentences = []
    sentence = []
    for line in lines:
        if 'EOS' in line:
            sentences.append(sentence)
            sentence = []
        elif '* ' in line:
            continue
        else:
            line_split = line.split('\t')
            surface = line_split[0]
            elems = line_split[1].split(',')
            morph = Morph(surface, elems[6], elems[0], elems[1])
            sentence.append(morph)
    f.close()
    return sentences

if __name__ == '__main__':
    sentences = read_cabocha_morph()
    for morph in sentences[2]:
        print(str(morph))

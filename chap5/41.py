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

if __name__ == '__main__':
    sentences = read_cabocha_chunk()
    for chunk in sentences[2]:
        print(str(chunk))

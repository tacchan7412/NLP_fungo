# coding: utf-8
import os, sys
sys.path.append(os.getcwd())

from modules import read_cabocha_chunk

def find_base_of_pos(morphs, pos):
    if pos == "動詞":
        for morph in morphs:
            if morph.pos == "動詞":
                return morph.base
    elif pos == "助詞":
        particles = []
        for morph in morphs:
            if morph.pos == "助詞":
                particles.append(morph.base)
        return particles
    return ""

def contains_pos(chunk, pos):
    return "pos: " + pos in str(chunk)

if __name__ == '__main__':
    fout = open('data/45.txt', 'w')
    sentences = read_cabocha_chunk()
    ans_dict = {}
    for sentence in sentences:
        for chunk in sentence:
            if chunk.dst != -1:
                if contains_pos(chunk, "助詞") and contains_pos(sentence[chunk.dst], "動詞"):
                    verb = find_base_of_pos(sentence[chunk.dst].morphs, "動詞")
                    particles = find_base_of_pos(chunk.morphs, "助詞")
                    if ans_dict.get(verb) is not None:
                        ans_dict[verb] += particles
                    else:
                        ans_dict[verb] = particles
    for key in ans_dict.keys():
        ans_dict[key] = sorted(ans_dict[key])
        fout.write(key + "\t" + " ".join(ans_dict[key]) + "\n")
    fout.close()

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
        all_morphs = ""
        list_of_tuple = []
        for morph in morphs:
            all_morphs += morph.surface
            if morph.pos == "助詞":
                particles.append(morph.base)
        for particle in particles:
            list_of_tuple.append((particle, all_morphs))
        return list_of_tuple
    return ""

def contains_pos(chunk, pos):
    return "pos: " + pos in str(chunk)

if __name__ == '__main__':
    fout = open('data/46.txt', 'w')
    sentences = read_cabocha_chunk()
    ans_dict = {}
    for sentence in sentences:
        for chunk in sentence:
            if chunk.dst != -1:
                if contains_pos(chunk, "助詞") and contains_pos(sentence[chunk.dst], "動詞"):
                    verb = find_base_of_pos(sentence[chunk.dst].morphs, "動詞")
                    list_of_set = find_base_of_pos(chunk.morphs, "助詞")
                    if ans_dict.get(verb) is not None:
                        ans_dict[verb] += list_of_set
                    else:
                        ans_dict[verb] = list_of_set
    for key, val in ans_dict.items():
        sorted_val = sorted(val, key=lambda x: x[0])
        morphs, all_morphs = [], []
        for tpl in sorted_val:
            morphs.append(tpl[0])
            all_morphs.append(tpl[1])
        fout.write(key + "\t" + " ".join(morphs) + "\t" + " ".join(all_morphs) + "\n")
    fout.close()

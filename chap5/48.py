# coding: utf-8
import os, sys
sys.path.append(os.getcwd())
args = sys.argv

from modules import read_cabocha_chunk

def extract_text(morphs):
    text = ""
    for morph in morphs:
        if morph.pos != "記号":
            text += morph.surface
    return text

def contains_pos(chunk, pos):
    return "pos: " + pos in str(chunk)

def get_path(chunk, sentence, text):
    text += extract_text(chunk.morphs)
    if chunk.dst == -1:
        return text
    else:
        return get_path(sentence[chunk.dst], sentence, text+" -> ")

if __name__ == '__main__':
    i = int(args[1])
    sentences = read_cabocha_chunk()
    for chunk in sentences[i]:
        if chunk.dst != -1:
            if contains_pos(chunk, "名詞"):
                print(get_path(chunk, sentences[i], ""))

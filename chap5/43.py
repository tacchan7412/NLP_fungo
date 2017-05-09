# coding: utf-8
import os, sys
sys.path.append(os.getcwd())

from modules import read_cabocha_chunk

def extract_text(morphs):
    text = ""
    for morph in morphs:
        if morph.pos != "記号":
            text += morph.surface
    return text

def contains_pos(chunk, pos):
    return "pos: " + pos in str(chunk)

if __name__ == '__main__':
    sentences = read_cabocha_chunk()
    concatenated_chunks = []
    for sentence in sentences:
        for chunk in sentence:
            if chunk.dst != -1:
                if contains_pos(chunk, "名詞") and contains_pos(sentence[chunk.dst], "動詞"):
                    srcs_text = extract_text(chunk.morphs)
                    dst_text = extract_text(sentence[chunk.dst].morphs)
                    concatenated_chunks.append(srcs_text + '\t' + dst_text)
    for chunk in concatenated_chunks:
        print(chunk)

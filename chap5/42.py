# coding: utf-8
import os, sys
sys.path.append(os.getcwd())

from modules import read_cabocha_chunk

def substract_text(morphs):
    text = ""
    for morph in morphs:
        if morph.pos != "記号":
            text += morph.surface
    return text

if __name__ == '__main__':
    sentences = read_cabocha_chunk()
    concatenated_chunks = []
    for sentence in sentences:
        for chunk in sentence:
            if chunk.dst != -1:
                srcs_text = substract_text(chunk.morphs)
                dst_text = substract_text(sentence[chunk.dst].morphs)
                if srcs_text != "" and dst_text != "":
                    concatenated_chunks.append(srcs_text + '\t' + dst_text)
    for chunk in concatenated_chunks:
        print(chunk)

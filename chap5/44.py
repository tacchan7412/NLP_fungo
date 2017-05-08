# coding: utf-8
import os, sys
sys.path.append(os.getcwd())
args = sys.argv

from modules import read_cabocha_chunk

def substract_text(morphs):
    text = ""
    for morph in morphs:
        if morph.pos != "記号":
            text += morph.surface
    return text

if __name__ == '__main__':
    i = int(args[1])
    fout = open('data/graph%d.dot'%i, 'w')
    fout.write("digraph g {\n")
    sentences = read_cabocha_chunk()
    for chunk in sentences[i]:
        if chunk.dst != -1:
            srcs_text = substract_text(chunk.morphs)
            dst_text = substract_text(sentences[i][chunk.dst].morphs)
            if srcs_text != "" and dst_text != "":
                fout.write("\t"+srcs_text+" -> "+dst_text+";\n")
    fout.write("}")
    fout.close()

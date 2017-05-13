# coding: utf-8
import os, sys
sys.path.append(os.getcwd())
args = sys.argv

from modules import read_cabocha_chunk

def extract_text(morphs, substitution):
    text = ""
    for morph in morphs:
        if morph.pos == "名詞" and substitution != "":
            text += substitution
        elif morph.pos != "記号":
            text += morph.surface
    return text

def contains_pos(chunk, pos):
    return "pos: " + pos in str(chunk)

def get_path_list(num, sentence, path_list):
    path_list.append(num)
    if sentence[num].dst == -1:
        return path_list
    else:
        return get_path_list(sentence[num].dst, sentence, path_list)

def get_path_for_true(path, sentence, start, end):
    text = ""
    for index in path:
        if index == end:
            return text + extract_text(sentence[index].morphs, "Y")
        elif index == start:
            text += extract_text(sentence[index].morphs, "X") + " -> "
        else:
            text += extract_text(sentence[index].morphs, "") + " -> "
    return ""

def get_path_for_false(path, sentence, start, end, substitution):
    text = ""
    for index in path:
        if index == end:
            return text.rstrip(" -> ")
        elif index == start:
            text += extract_text(sentence[index].morphs, substitution) + " -> "
        else:
            text += extract_text(sentence[index].morphs, "") + " -> "
    return ""

if __name__ == '__main__':
    paths = []
    sentences = read_cabocha_chunk()
    sentence = sentences[int(args[1])]
    for i in range(len(sentence)):
        if sentence[i].dst != -1:
            if contains_pos(sentence[i], "名詞"):
                paths.append(get_path_list(i, sentence, []))

    for i in range(len(paths)):
        for j in range(i+1, len(paths)):
            if paths[j][0] in paths[i]:
                print(get_path_for_true(paths[i], sentence, paths[i][0], paths[j][0]))
            else:
                end = list(set(paths[i])&set(paths[j]))[0]
                output_text = get_path_for_false(paths[i], sentence, paths[i][0], end, "X") + " | "
                output_text += get_path_for_false(paths[j], sentence, paths[j][0], end, "Y") + " | "
                output_text += extract_text(sentence[end].morphs, "")
                print(output_text)

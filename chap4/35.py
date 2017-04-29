# coding: utf-8
import os, sys
sys.path.append(os.getcwd())

from modules import read_mecab

noun_indication = 'DELETETHIS'

if __name__ == '__main__':
    result_set = set()
    morphologies = read_mecab()

    for sentence in morphologies:
        sentence_copy = ''
        for i in range(len(sentence)):
            if sentence[i]['pos'] == '名詞':
                sentence_copy += noun_indication
                sentence_copy += sentence[i]['surface']
            else:
                sentence_copy += '|'
        articulations = sentence_copy.split('|')
        for articulation in articulations:
            if articulation != '' and len(articulation.split(noun_indication)) > 2:
                result_set.add(articulation.replace(noun_indication, ''))
    print(result_set)

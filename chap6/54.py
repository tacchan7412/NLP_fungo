# coding: utf-8
import os, sys
sys.path.append(os.getcwd())

import xml.etree.ElementTree as ET

if __name__ == '__main__':
    tree = ET.parse('data/nlp.txt.xml')
    root = tree.getroot()
    word_list= root.findall(".//word")
    lemma_list = root.findall(".//lemma")
    pos_list = root.findall(".//POS")
    for word, lemma, pos in zip(word_list, lemma_list, pos_list):
        print('%s\t%s\t%s'%(word.text, lemma.text, pos.text))

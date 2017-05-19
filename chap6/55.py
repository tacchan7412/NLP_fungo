# coding: utf-8
import os, sys
sys.path.append(os.getcwd())

import xml.etree.ElementTree as ET

if __name__ == '__main__':
    tree = ET.parse('data/nlp.txt.xml')
    root = tree.getroot()
    word_list = root.findall(".//word")
    ner_list = root.findall(".//NER")
    for word, ner in zip(word_list, ner_list):
        if ner.text == 'PERSON':
            print(word.text)

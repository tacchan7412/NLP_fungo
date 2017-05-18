# coding: utf-8
import os, sys
sys.path.append(os.getcwd())

import xml.etree.ElementTree as ET

if __name__ == '__main__':
    tree = ET.parse('data/nlp.txt.xml')
    root = tree.getroot()
    elem_list = root.findall(".//word")
    for elem in elem_list:
        print(elem.text)

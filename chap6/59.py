# coding: utf-8
import os, sys
sys.path.append(os.getcwd())

import xml.etree.ElementTree as ET
import re

def get_NP(text, NP_list):
    re_text = re.search('\((.*?)\s(.*)\)', text)
    tag = re_text.group(1)
    value = re_text.group(2)
    cnt = 0
    chunk = ''
    words = []

    for letter in value:
        if letter == '(':
            cnt+=1
            chunk+=letter
        elif letter == ')':
            cnt-=1
            chunk+=letter
            if cnt == 0:
                words.append(get_NP(chunk, NP_list))
                chunk = ''
        elif letter == ' ' and cnt == 0:
            continue
        else:
            chunk+=letter

    if chunk != '':
        words.append(chunk)

    result = ' '.join(words)

    if tag == 'NP':
        result = result.replace('-LRB- ', '(', len(result))
        result = result.replace(' -RRB-', ')', len(result))
        NP_list.append(result)

    return result



if __name__ == '__main__':
    tree = ET.parse('data/nlp.txt.xml')
    root = tree.getroot()
    parses = root.findall(".//parse")
    for parse in parses:
        ans_list = []
        get_NP(parse.text, ans_list)
        print('\n'.join(ans_list))

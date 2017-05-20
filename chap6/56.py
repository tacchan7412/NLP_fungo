# coding: utf-8
import os, sys
sys.path.append(os.getcwd())

import xml.etree.ElementTree as ET

if __name__ == '__main__':
    tree = ET.parse('data/nlp.txt.xml')
    root = tree.getroot()

    # coreference一覧の取得
    coreference_list = root.findall(".//coreference/coreference")
    coreference_detail_list = []
    for coreference in coreference_list:
        mentions = coreference.findall(".//mention")
        text = ""
        for mention in mentions:
            if mention.attrib.get("representative") == "true":
                text = mention.find(".//text").text
                text = text.replace('-LRB- ', '(')
                text = text.replace(' -RRB-', ')')
            else:
                sentence = int(mention.find(".//sentence").text)
                start = int(mention.find(".//start").text)
                end = int(mention.find(".//end").text)
                coreference_detail_list.append((sentence, start, end, text))

    # word一覧の取得
    sentence_list = root.findall(".//sentences/sentence")
    for i, sentence in enumerate(sentence_list):
        words = sentence.findall(".//token/word")
        text = []
        for word in words:
            if word.text == '-LRB-':
                text.append('(')
            elif word.text == '-RRB-':
                text.append(')')
            else:
                text.append(word.text)


        for detail in coreference_detail_list:
            if i+1 == detail[0]:
                text[detail[1]-1] = detail[3] + '(' + text[detail[1]-1]
                text[detail[2]-2] += ')'

        raw_text = " ".join(text)
        raw_text = raw_text.replace(' ,', ',', len(raw_text))
        raw_text = raw_text.replace(' .', '.', len(raw_text))
        raw_text = raw_text.replace('( ', '(', len(raw_text))
        raw_text = raw_text.replace(' )', ')', len(raw_text))
        raw_text = raw_text.replace(" ''", '"', len(raw_text))
        raw_text = raw_text.replace('`` ', '"', len(raw_text))
        raw_text = raw_text.replace(" '", "'", len(raw_text))
        raw_text = raw_text.replace('` ', "'", len(raw_text))
        
        print(raw_text)

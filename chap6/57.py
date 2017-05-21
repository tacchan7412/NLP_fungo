# coding: utf-8
import os, sys
sys.path.append(os.getcwd())
args = sys.argv

import xml.etree.ElementTree as ET

if __name__ == '__main__':
    i = int(args[1])
    fout = open('data/graph_English%d.dot'%i, 'w')
    fout.write("digraph g {\n")
    tree = ET.parse('data/nlp.txt.xml')
    root = tree.getroot()
    collapsed_dependencies = root.findall(".//dependencies[@type='collapsed-dependencies']")
    deps = collapsed_dependencies[i].findall(".//dep")
    for dep in deps:
        governor = dep.find(".//governor").text
        dependent = dep.find(".//dependent").text
        if dependent == '-LRB-':
            dependent = '('
        elif dependent == '-RRB-':
            dependent = ')'
        if dependent != '.' and dependent != ',':
            fout.write("\t"+'"'+governor+'"'+" -> "+'"'+dependent+'"'+";\n")
    fout.write("}")
    fout.close()

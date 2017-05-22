# coding: utf-8
import os, sys
sys.path.append(os.getcwd())

import xml.etree.ElementTree as ET

if __name__ == '__main__':
    tree = ET.parse('data/nlp.txt.xml')
    root = tree.getroot()
    collapsed_dependencies = root.findall(".//dependencies[@type='collapsed-dependencies']")
    for collapsed_dependency in collapsed_dependencies:
        nsubj_deps = collapsed_dependency.findall(".//dep[@type='nsubj']")
        nsubj_dict = {}
        dobj_deps = collapsed_dependency.findall(".//dep[@type='dobj']")
        dobj_dict = {}
        for nsubj_dep in nsubj_deps:
            governor = nsubj_dep.find(".//governor").text
            dependent = nsubj_dep.find(".//dependent").text
            nsubj_dict[governor] = dependent
        for dobj_dep in dobj_deps:
            governor = dobj_dep.find(".//governor").text
            dependent = dobj_dep.find(".//dependent").text
            if nsubj_dict.get(governor) is not None:
                print('%s\t%s\t%s' %(nsubj_dict[governor], governor, dependent))

# coding: utf-8
import os, sys
sys.path.append(os.getcwd())

import codecs

if __name__ == '__main__':
    f = codecs.open('data/80.txt')
    f_country = codecs.open('data/country_names.txt')
    lines = f.readlines()
    countries = f_country.readlines()
    f.close()
    f_country.close()
    countries_ = []
    for country in countries:
        name = country.split(' ')
        if len(name) > 1:
            country_ = '_'.join(name)
            countries_.append(country_[:-1])

    f_out = codecs.open('data/81.txt', 'w')
    for line in lines:
        for country_ in countries_:
            print(country_)
            line = line.replace(' '.join(country_.split('_')), country_, len(line))
        f_out.write(line)
    f_out.close()

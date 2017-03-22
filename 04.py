# coding: utf-8

str = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
one_index = [1, 5, 6, 7, 8, 9, 15, 16, 19]

if __name__ == '__main__':
    str = str.replace(",", "", len(str)).replace(".", "", len(str))
    word_list = str.split(" ")
    map = {}
    for i in range(len(word_list)):
        if i + 1 in one_index:
            word = word_list[i][:1]
        else:
            word = word_list[i][:2]
        map[word] = i + 1
    print(map)

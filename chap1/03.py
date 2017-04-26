# coding: utf-8

str = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."

if __name__ == '__main__':
    str = str.replace(",", "", len(str)).replace(".", "", len(str))
    word_list = str.split(" ")
    word_len_list = [len(word) for word in word_list]
    print(word_len_list)

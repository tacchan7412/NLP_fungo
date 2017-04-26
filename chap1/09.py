# coding: utf-8

import random

str = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."

if __name__ == '__main__':
    word_list = str.split(" ")
    output_list = []
    for word in word_list:
        if len(word) > 4:
            listed_word = list(word[1:len(word) - 1])
            random.shuffle(listed_word)
            output_list.append(word[0] + "".join(listed_word) + word[len(word) - 1])
        else:
            output_list.append(word)

    print(" ".join(output_list))

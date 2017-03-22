# coding: utf-8

str = "I am an NLPer"

def ngram(sequence, n):
    output_list = []
    for i in range(len(sequence) - n + 1):
        output = sequence[i:i + n]
        output = "".join(output)
        output_list.append(output)
    return output_list

if __name__ == '__main__':
    str_for_word_list = str.split(" ")
    print(ngram(str_for_word_list, 2))

    str_for_letter = str.replace(" ", "", len(str))
    print(ngram(str_for_letter, 2))

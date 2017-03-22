# coding: utf-8

str1 = "paraparaparadise"
str2 = "paragraph"

def ngram(sequence, n):
    output_list = []
    for i in range(len(sequence) - n + 1):
        output = sequence[i:i + n]
        output = "".join(output)
        output_list.append(output)
    return output_list

if __name__ == '__main__':
    str1 = str1.replace(" ", "", len(str1))
    str2 = str2.replace(" ", "", len(str2))

    X = ngram(str1, 2)
    Y = ngram(str2, 2)

    X = set(X)
    Y = set(Y)

    print(X & Y)
    print(X | Y)
    print(X - Y)

    print("'se' in X: " + str('se' in X))
    print("'se' in Y: " + str('se' in Y))

# coding: utf-8

str1 = "パトカー"
str2 = "タクシー"

if __name__ == '__main__':
    str = ""
    for i in range(4):
        str += str1[i] + str2[i]
    print(str)

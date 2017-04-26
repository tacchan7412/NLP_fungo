# coding: utf-8

def cipher(str):
    output_str = ""
    for letter in str:
        if letter.isalnum() and not letter.isupper():
            output_str += chr(217 - ord(letter.encode('utf-8')))
        else:
            output_str += letter
    return output_str

if __name__ == '__main__':
    str = "I have a pen. I have an apple."
    print(cipher(str))
    print(cipher(cipher(str)))

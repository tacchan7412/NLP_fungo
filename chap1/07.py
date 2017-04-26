# coding: utf-8

def temp_generator(x, y, z):
    return str(x) + "の時の" + str(y) + "は" + str(z)

if __name__ == '__main__':
    x, y, z = 12, "気温", 22.4
    print(temp_generator(x, y, z))

# coding: utf-8

if __name__ == '__main__':
    # 1列目のみを読み取る
    f = open('hightemp.txt', 'r')
    lines = f.readlines()
    set_for_col1 = set()
    for line in lines:
        cols = line.split('\t')
        set_for_col1.add(cols[0])
    f.close()
    print(set_for_col1)

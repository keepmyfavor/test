# -*- coding:UTF-8 -*-

def oddandeven():
    num = int(input("請輸入1~1000的整數:"))
    if 0 < num <= 1000:
        if num % 2 == 0:
            print("%d 是一個偶數" % num)
        else:
            print("%d 是一個奇數" % num)
    else:
        print("%d 超過範圍" % num)


if __name__ == '__main__':
    oddandeven()

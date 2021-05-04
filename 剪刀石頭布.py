# -*- coding:UTF-8 -*-
import random


def puncher(num):
    if num == 1:
        return "剪刀"
    elif num == 2:
        return "石頭"
    else:
        return "布"


def result():
    punch = int(input("請出拳: 1 = 剪刀 , 2 = 石頭 , 3 = 布 "))
    if punch == 1 or punch == 2 or punch == 3:
        pcpunch = random.randint(1, 3)
        if punch == pcpunch:
            print("電腦出\t%s \n您出\t\t%s \n結果 \t平手" % (puncher(pcpunch), puncher(punch)))
        elif (punch == 1 and pcpunch == 3) or (punch == 2 and pcpunch == 1) or (punch == 3 and pcpunch == 2):
            print("電腦出\t%s \n您出\t\t%s \n結果 \t您勝利了" % (puncher(pcpunch), puncher(punch)))
        else:
            print("電腦出\t%s \n您出\t\t%s \n結果 \t您輸了" % (puncher(pcpunch), puncher(punch)))
    else:
        print("輸入錯誤,請重新輸入")


if __name__ == '__main__':
    while True:
        result()
        getcode = input("任意鍵繼續或結束遊戲(n)")
        if getcode == "n" or getcode == "N":
            print("遊戲結束")
            break

import random

total = "123456789"
answer = random.sample(total, 4)
print(total, "\n", answer)
for guessTimes in range(6):
    guess = ""
    for inputError in range(3):
        guess = input("請輸入4位1~9的不重複數字:")
        if guess.isdigit() == True and len(set(guess)) == 4 and set(guess).isdisjoint("0") == True:
            print(guess)
            break
        else:
            print("輸入格式錯誤%d次, 剩下%d次機會" % (inputError + 1, 2 - inputError))
    else:
        print("您沒有理解遊戲規則,遊戲結束")
        break
    A = 0
    B = 0
    for j in range(4):
        if guess[j] == answer[j]:
            A += 1
        else:
            for k in range(4):
                if guess[j] == answer[k]:
                    B += 1
    if A < 4:
        if guessTimes == 5:
            print("遊戲結束, 答案是%s" % answer)
        else:
            print("%dA%dB, 加油, 還有%d次機會" % (A, B, 5 - guessTimes))
    else:
        print("%dA%dB, 猜中了" % (A, B))
        break




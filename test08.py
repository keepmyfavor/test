import random
print("/*******************************猜數字遊戲***********************************/ \
   遊戲規則：系統隨機給出1-9的4位數字，您可以輸入您猜測的4位數字，系統會比較並給予反饋，A表示數字對，且位置對，B表示數字對位置不對，如1A2B表示有1位您猜對了數字和位置，有2位您猜對數字，但位置不對。您總共有6次機會，加油哦！")
total='123456789'
answer=random.sample(total,4)
for guessTimes in range(6):
   guess=""
   for inputErros in range(3):
      guess=input("請輸入4位1-9的不重複數字：")
      if guess.isdigit()==True and len(guess)==4:
         guessSet=set(guess)
         if len(guessSet)==4 and guessSet.isdisjoint(set('0')):
            break
   else:
      print("您沒有理解遊戲規則，遊戲結束。")
      break
   A=0
   B=0
   for j in range(4):
      if guess[j]==answer[j]:
         A+=1
      else:
         for k in range(4):
            if guess[j]==answer[k]:
               B+=1
   if A<4:
      if guessTimes<5:
         print("%dA%dB，您還有%d次機會。" %(A,B,5-guessTimes))
      else:
         print("很遺憾您沒有猜對，答案是%s，再玩一局吧。" %(answer))
   else:
      print("恭喜您猜對了！")
      break

heads, legs = map(int, input("請輸入雞兔總數和腿總數: ").split())

rabbit = (legs - heads * 2) / 2

chicken = heads - rabbit

if rabbit >= 0 and chicken >= 0 and int(rabbit) == rabbit:
    print("雞: {}, 兔: {}".format(int(chicken), int(rabbit)))
else:
    print("數據不正確")

'''
head = int(input("請輸入雞兔隻數: "))
foot = int(input("請輸入雞兔腳數: "))

y = (foot - 2 * head) / 2
x = head - y

if x * 2 + y * 4 == foot and y >= 0:
    print("雞 %d 隻 兔 %d 隻" % (x, y))
else:
    print("輸入的資料錯誤")

'''

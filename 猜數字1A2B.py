import random

# 抓取 "123456789" 中的4個不重覆的字串
x = random.sample("123456789", 4)
# x = ["1", "3", "5", "7"]
print(x)

while True:
    y = input("請輸入4個不同的數字(0~9):")
    # y 集合的長度 及 y 的長度
    if len(set(y)) == 4 and len(y) == 4:
        # print(set(y))
        # print(y)
        # 將輸入的數字轉為字串
        z = list(y)
        print(z)
        a = 0
        # 字串比對,位置及數字一樣的就+1
        for i in range(4):
            if x[i] == z[i]:
                a += 1
        # 集合(x) 減去 集合(z) 就是只有一樣的數字
        # -a 就是減去相同位置且相同數字的
        b = 4 - len(set(x) - set(z)) - a
        # print(set(x), set(z))
        print("%d A %d B" % (a, b))
        if a == 4:
            break
    else:
        print("輸入誤錯")

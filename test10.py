def app(a, b):
    x = (4 * a - b) / 2
    if a != 0 and (4 * a - b) % (x * 2) == 0:
        y = a - x
        if x < 0 or y < 0:
            print("{}隻動物{}條腿的情況無解".format(a, b))
        else:
            print("雞有{}隻, 免有{}隻".format(int(x), int(y)))
    else:
        print("{}隻動物{}條腿的情況無解".format(a, b))

a = input("請輸入總數\n")
b = input("請輸入腿數\n")

a = int(a)
b = int(b)
app(a, b)



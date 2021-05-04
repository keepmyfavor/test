# -*- coding:UTF-8 -*-

import math

print(math.pow(2, 3))
print(math.sqrt(4))

x1, y1 = 10, 20
x2, y2 = 15, 45

x = math.pow((x1 - x2), 2)
y = math.pow((y1 - y2), 2)

d = math.sqrt(x + y)
print("x = %d \ny = %d \nd = %.1f" % (x, y, d))

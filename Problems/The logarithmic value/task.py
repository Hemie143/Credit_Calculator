from math import log
a = int(input())
b = int(input())
if b < 2:
    print(round(log(a), 2))
else:
    print(round(log(a, b), 2))

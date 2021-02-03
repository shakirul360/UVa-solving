import math
n = int(input())

i=1
while i<=n:
    x = int(input())
    res = (-1 + math.sqrt(1 + 8 * x)) / 2
    print(int(res))
    i = i+1

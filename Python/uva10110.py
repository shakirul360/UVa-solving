import math

while True:
    n = int(input())
    if n == 0:
        break
    else:
        s_n = int(math.sqrt(n))
        if (s_n * s_n) == n:
            print("yes")
        else:
            print("no")

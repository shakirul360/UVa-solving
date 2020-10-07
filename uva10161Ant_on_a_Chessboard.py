from math import ceil
from math import sqrt
while True:
    n = int(input())
    if n == 0:
        break
    
    root = ceil(sqrt(n))
    c = root * root - root + 1
    x = y = root
    
    if (root % 2) == 0:
        if n > c:
            y -= n - c
        else:
            x -= c - n
    else:
        if (n > c):
            x -= n - c
        else:
            y -= c - n
    
    print(x,y)

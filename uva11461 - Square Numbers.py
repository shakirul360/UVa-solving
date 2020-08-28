import math

while True:
    a, b = map(int,input().split())
    total = 0
    if a == 0 and b == 0:
        break
    for i in range(a,b + 1):
        root = math.sqrt(i)
        if root == int(root):
            total += 1
            #print(root)
    print(total)

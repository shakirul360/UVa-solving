T = int(input())
for _ in range(T):
    a,b = map(int,input().split())
    ###a = sum, b = abs.difference
    y = abs(a-b)//2
    x = a -y
    
    if (x+y) == a and abs(x-y)==b:
        print("{} {}".format(max(x,y),min(x,y)))

    else:
        print("impossible")

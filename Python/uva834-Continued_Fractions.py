while True:
    try:
        n, d = map(int,input().split())
    except:
        break
    r = n // d
    temp = n
    n = d
    d = temp - (d * r)
    print("[{};".format(r),end = '')
    while n > 1 and d > 0:
        #print(r,n,d)
        r = n // d
        temp = n
        n = d
        d=temp-(d*r)
        if(n>1) and d > 0:
                print("{},".format(r), end = '')
        else:
                print("{}".format(r), end = '')
    print("]")

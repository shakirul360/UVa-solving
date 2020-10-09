case = 1
while True:
    z, i, m, l = map(int,input().split())
    if z == 0 and i == 0 and  m == 0 and l == 0:
        break
    arr = []
    seed = l
    while True:
        res = (z * l + i) % m
        if res in arr:
            break
        elif res == seed:
            arr.append(res)
            break
        else:
            arr.append(res)
        l = res
    print("Case  {}:  {}".format(case,len(arr)))
    case += 1
    #print(arr)

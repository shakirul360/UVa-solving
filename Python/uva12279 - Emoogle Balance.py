case = 1
while True:
    tcases = int(input())
    if tcases == 0:
        break
    emoogle = 0
    arr = list(map(int,input().split()))
    for i in arr:
        if i == 0:
            emoogle -= 1
        else:
            emoogle += 1
    print("Case {}: {}".format(case,emoogle))
    case += 1

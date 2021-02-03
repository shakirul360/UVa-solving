while True:
    n = int(input())
    if n < 0:
        break
    res = 0
    if n > 1:
        res = n * 25
    
    print("{}%".format(res))

while True:
    n = int(input())
    if n == 0:
        break
    arr = sorted(list(map(int,input().split())))
    total = 0
    while len(arr) > 1:
        add = arr[0] + arr[1]
        arr.pop(0)
        arr.pop(0)
        arr.append(add)
        total += add
        arr = sorted(arr)
    
    print(total)

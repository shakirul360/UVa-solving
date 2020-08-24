while True:
    try:
        n = int(input())
    except EOFError:
        break
    arr = list(map(int,input().split()))
    flip = 0 
    for i in range(n-1): 
        for j in range(0, n-i-1): 
            if arr[j] > arr[j+1] : 
                arr[j], arr[j+1] = arr[j+1], arr[j]
                flip += 1
    print("Minimum exchange operations : {}".format(flip))

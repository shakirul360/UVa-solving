while True:
    thrown = []
    n = int(input())
    if n == 0:
        break
    arr = [i for i in range(1, n + 1)]

    while len(arr) > 1:
        try:    
            thrown.append(arr.pop(0))
            arr.append(arr.pop(0))
        except:
            break
    if len(thrown) == 0:
            print("Discarded cards:", end = '')
    else:
        print("Discarded cards: ", end = '')
    print(*thrown, sep = ', ')
    print("Remaining card: {}".format(arr[0]))

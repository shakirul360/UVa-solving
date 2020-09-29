while True:
    try:
        n = int(input())
        book_prices = sorted(list(map(int,input().split())))
        total = int(input())
        x = input()
    except EOFError:
        break
    #print(book_prices)
    
    a, b  = None, None
    abss = 1000001
    for i in book_prices:
        j = total - i
        if j in book_prices:
            if abs(i-j) < abss:
                a, b = i,j
                abss = abs(i - j)
    print("Peter should buy books whose prices are {} and {}.".format(a,b))
    print(x)

while True:
    try:
        n = int(input())
        book_prices = sorted(list(map(int,input().split())))
        total = int(input())
        x = input()
    except EOFError:
        break
    
    i = 0
    j = n - 1
    a, b = 0, 0
    while i < j:
        if(book_prices[i] + book_prices[j] < total):
            i += 1
        elif book_prices[i] + book_prices[j] == total:
            a = i
            b = j
            i += 1
            j -= 1
        else:
            j -= 1    
    print("Peter should buy books whose prices are {} and {}.".format(book_prices[a],book_prices[b]))
    print(x)

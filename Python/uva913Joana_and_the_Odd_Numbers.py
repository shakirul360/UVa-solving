while True:
    try:
        n = int(input())
    except EOFError:
        break
    
    n = (n + 1) // 2
    last = 2 * (pow(n, 2)) - 1
    total = (3 * last) - 6
    print(total)

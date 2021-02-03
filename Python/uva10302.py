while True:
    try:
        n = int(input())
    except EOFError:
        break
    total = 0
    for i in range(n+1):
        total += (i**3)
    print(total)

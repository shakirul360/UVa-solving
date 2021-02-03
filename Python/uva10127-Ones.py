def getdigitcount(n):
    current = 1
    digitcount = 1
    while current % n != 0:
        current = current * 10 + 1
        digitcount += 1
        
    print(digitcount)
        
while True:
    try:
        n = int(input())
    except EOFError:
        break
    getdigitcount(n)

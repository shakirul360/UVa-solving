def coke(n):
    total = 0
    while n > 1:
        if n == 2:
            n += 1
        if n >= 3:
            total += n // 3
            n = n // 3 + n % 3
    print(total)

while True:
    n = int(input())
    if not n:
        break
    coke(n)

def bottles(n,p):
    total = 0
    while n >= p:
        total += n // p
        n = (n % p) + (n // p)
    print(total)

tcase = int(input())
for case in range(tcase):
    e, f, c = map(int,input().split())
    n = e + f
    bottles(n,c)

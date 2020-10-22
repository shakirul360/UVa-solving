while True:
    h1, m1, h2, m2 = map(int,input().split())
    if h1 == 0 and m1 == 0 and h2 == 0 and m2 == 0:
        break
    if(h1 > h2 or h1 == h2 and m1 > m2):
        h2 += 24
    print(60 * ( h2 - h1 ) + m2 - m1)

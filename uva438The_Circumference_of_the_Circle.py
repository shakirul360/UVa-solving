from math import pi,sqrt
while True:
    try:
        x1, y1, x2, y2, x3, y3 = list(map(float,input().split()))
    except EOFError:
        break
    a = sqrt( pow(x1 - x2, 2) + pow(y1 - y2, 2) )
    b = sqrt( pow(x2 - x3, 2) + pow(y2 - y3, 2) )
    c = sqrt( pow(x3 - x1, 2) + pow(y3 - y1, 2) )

    s = ( a + b + c ) / 2
    A = sqrt(s*(s-a)*(s-b)*(s-c))
    d = (a * b * c) / (2 * A)

    circumference = pi * d

    print(round(circumference,2))

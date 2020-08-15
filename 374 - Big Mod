def formula(b, p, m):
    if p == 0:
        return 1
    elif p == 1:
        return b % m
    else:
        res = formula(b, p//2, m)
        if p % 2:
            return res * res * b % m
        else:
            return res * res % m
			
while True:
    try:
        b = input()
        if b == "":
            b = int(input())
        else:
            b = int(b)

        p = int(input())
        m = int(input())
    except EOFError:
        break

    print(formula(b, p, m))

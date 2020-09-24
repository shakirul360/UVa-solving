def solve(n,m):
    if n > m:
        n, m = m, n
    if n == 1:
        return m
    elif n == 2:
        x = m % 4
        if x == 1:
            return m // 4 * 4 + 2
        elif x >= 2:
            return m // 4 * 4 + 4
        else:
            return m // 4 * 4
    else:
        return (n*m + 1) // 2
    
while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    print("{} knights may be placed on a {} row {} column board.".format(solve(n,m), n, m))
    

def solve(a, b, c):
    for i in range(0, 100):
        for j in range(0,100):
            for k in range(0,100):
                if (i!=j and j!=k and i!=k) and (i+j+k == a and i*j*k == b and i*i+j*j+k*k == c):
                    return i, j, k
    return False

tcase = int(input())
for case in range(tcase):
    a, b, c = map(int,input().split())
    if solve(a, b, c) == False:
        print("No solution.")
    else:
        print(*solve(a,b,c))
        #print(type(solve(1,2,3)))

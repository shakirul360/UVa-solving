n = int(input())
for i in range(n):
    a, b = input().split()
    a = int((a)[::-1])
    b = int((b)[::-1])
    res = a + b
    res_rev = str(res)[::-1]
    #print(a,b)
    print(int(res_rev))

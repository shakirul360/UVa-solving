n = int(input())
for i in range(n):
    a, b = input().split()
    len_diff = abs(len(a) - len(b))
    if len(b) > len(a):
        a, b = b, a
        b = b.ljust(len_diff + len(b), '0')
    else:
        b = b.ljust(len_diff + len(b), '0')
    print(a,b)
    a = a[::-1]
    b = b[::-1]
    print(a,b)
    res = ''
    for num in range(len(a)):
        res += str(int(a[num]) + int(b[num]))
    print(res)

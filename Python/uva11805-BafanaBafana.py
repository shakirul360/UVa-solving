tcase = int(input())
for i in range(tcase):
    n, k, p = map(int,input().split())
    ans = (k + p) % n
    #print(ans)
    if ans == 0:
        print("Case {}: {}".format(i + 1, n))
    else:
        print("Case {}: {}".format(i + 1, ans))

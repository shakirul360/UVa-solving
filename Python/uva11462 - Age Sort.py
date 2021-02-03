while True:
    n = int(input())
    if n == 0:
        break
    arr = map(int,input().split())
    print(*sorted(arr))

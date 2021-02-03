tcases = int(input())
for _ in range(tcases):
    n = int(input())
    arr = list(map(int,input().split()))
    high = max(arr)
    low = min(arr)
    dist = 2 * (high - low)
    print(dist)

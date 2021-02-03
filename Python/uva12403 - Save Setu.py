total = 0
n = int(input())
for _ in range(n):
    arr = list(input().split())
    #print(arr)
    if arr[0] == "report":
        print(total)
    else:
        money = int(arr[1])
        total += money

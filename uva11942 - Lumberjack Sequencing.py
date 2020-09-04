n = int(input())
print("Lumberjacks:")
for i in range(n):
    arr = list(map(int,input().split()))
    asc_arr = sorted(arr)
    des_arr = reversed(asc_arr)
    #print(asc_arr)
    #print(asc_arr.reverse())
    if arr == asc_arr:
        print("Ordered")
    else:
        asc_arr.reverse()
        if arr == asc_arr:
            print("Ordered")
        else:
            print("Unordered")

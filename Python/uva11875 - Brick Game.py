tcases = int(input())
for i in range(tcases):
    arr = list(map(int,input().split()))
    n = arr.pop(0)
    arr  = sorted(arr)
    #print(arr)
    x = arr[len(arr)//2]
    print("Case {}: {}".format(i+1,x))

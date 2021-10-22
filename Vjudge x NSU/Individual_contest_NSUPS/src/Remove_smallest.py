tcase = int(input())

for i in range(tcase):
    n = int(input())
    arr = [int(x) for x in input().split()]
    
    arr.sort()
    flag = True;
    
    while (len(arr) != 1 and flag == True):
        if (arr[1] - arr[0] == 1 or arr[1] - arr[0] == 0):
            arr.pop(0)
        else:
            flag = False
            break
    
    if flag:
        print("YES")
    else:
        print("NO")
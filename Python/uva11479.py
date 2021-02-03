tcase = int(input())
for i in range(tcase):
    arr = list(map(int, input().split()))
    arr = sorted(arr)
    if arr[0] + arr[1] <= arr[2]:
        print("Case {}: Invalid".format(i + 1))
    else:
        if arr[0] == arr[1] == arr[2]: 
            print("Case {}: Equilateral".format(i + 1)) 
  
        elif arr[0] == arr[1] or arr[1] == arr[2] or arr[2] == arr[0]: 
            print("Case {}: Isosceles".format(i + 1)) 
  
        else: 
            print("Case {}: Scalene".format(i + 1)) 

n = int(input())
for _ in range(n):
    arr = []
    integer = int(input())
    for i in range(1,integer + 1):
        arr.append(str(i))
    string = "".join(arr)
    num_count = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for j in string:
        num_count[int(j)] += 1
    print(*num_count)
        
        
        

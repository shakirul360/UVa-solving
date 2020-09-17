case = 0
while True:
    n, q = map(int,input().split())
    if not n and not q:
        break
    arr = []
    for _ in range(n):
        arr.append(int(input()))
    arr = sorted(arr)
    #print(arr)
    print("CASE# {}:".format(case + 1))
    case += 1
    for i in range(q):
        query = int(input())
        if query not in arr:
            print("{} not found".format(query))
        else:
            traversal = 1
            for x in arr:
                if x == query:
                    print("{} found at {}".format(query,traversal))
                    break
                else:
                    traversal += 1

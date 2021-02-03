while True:
    heads = []
    soldier_heights = []
    head_count, soldiers = map(int,input().split())
    if not head_count and not soldiers:
        break
    for head in range(head_count):
        heads.append(int(input()))
    for soldier in range(soldiers):
        soldier_heights.append(int(input()))
    
    res = 0
    heads.sort()
    soldier_heights.sort()
    #print(heads)
    #print(soldier_heights)
    for i in soldier_heights:
        for j in heads:
            if i == j or i > j:
                #print(i, j)
                res += i
                heads.remove(j)
                #print(heads)
                #print(soldier_heights)
    
    if not heads:    
        print(res)
    else:
        print("Loowater is doomed!")

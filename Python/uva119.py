c = 0
while True:
    records = {}
    try:
        n = int(input())
    except EOFError:
        break
    names = list(input().split())
    for name in names:
        records[name] = 0
    #print(records)
    
    for i in range(n):
        arr = list(input().split())
        spent, donee_num = arr[1], arr[2]
        spent, donee_num = int(spent), int(donee_num)
        if donee_num != 0:
            add = spent // donee_num
            sub = spent - (spent % donee_num)
            for j in range(donee_num):
                records[arr[3+j]] += add
            records[arr[0]] -= sub
            
    if c > 0:
        print()
    for key, value in records.items():
        print("{} {}".format(key, value))
    c += 1

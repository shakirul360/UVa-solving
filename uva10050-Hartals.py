tcase = int(input())
for case in range(tcase):
    days = int(input())
    arr = [0 for i in range(days + 1)]
    parties = int(input())
    for i in range(parties):
        party = int(input())
        for j in range(party, days + 1, party):
            arr[j] = 1
    try:
        for x in range(6, days + 1, 7):
            arr[x] = 0
            arr[x + 1] = 0
    except:
        pass
    print(sum(arr))

tcase = int(input())
for case in range(tcase):
    dicts = {}
    for q in range(10):
        s = list(input().split())
        relevance = int(s.pop())
        if relevance in dicts:
            dicts[relevance].append(s[0])
        else:
            dicts[relevance] = [s[0]]
    #print(dicts)
    x = sorted(dicts.items())
    print("Case #{}:".format(case + 1))
    for i in x[-1][-1]:
        print(i)
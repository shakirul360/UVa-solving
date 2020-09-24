n = int(input())
for i in range(n):
    arr = []
    t1, t2, final, att, c1, c2, c3 = map(int, input().split())
    arr.append(c1)
    arr.append(c2)
    arr.append(c3)
    arr.sort()
    avg = (arr[-1] + arr[-2]) // 2
    #print(arr[-1], arr[-2])
    total = t1 + t2 + final + att + avg
    #print(total)
    if total >= 90:
        print("Case {}: A".format(i + 1))
    elif total >= 80:
        print("Case {}: B".format(i + 1))
    elif total >= 70:
        print("Case {}: C".format(i + 1))
    elif total >= 60:
        print("Case {}: D".format(i + 1))
    else:
        print("Case {}: F".format(i + 1))

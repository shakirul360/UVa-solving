tcase = int(input())
for case in range(tcase):
    #month = 0
    blank = input()
    d1, m1, y1 = map(int,input().split("/"))
    d2, m2, y2 = map(int,input().split("/"))
    if d1 < d2:
        m2 += 1
    if m1 < m2:
        y2 += 1
    age = y1 - y2
    if age < 0:
        print("Case #{}: Invalid birth date".format(case + 1))
    elif age > 130:
        print("Case #{}: Check birth date".format(case + 1))
    else:
        print("Case #{}: {}".format(case + 1, age))

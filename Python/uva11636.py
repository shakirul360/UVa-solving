case = 1
while True:
    value = 1
    count = 0
    n = int(input())
    if n < 0:
        break
    while value < n:
        value *= 2
        count += 1
    print("Case {}: {}".format(case,count))
    case += 1

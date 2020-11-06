case = 1
while True:
    n = int(input())
    if n == 0:
        break
    arr = []
    for i in range(n):
        arr.append(int(input()))
    print("Case {}:".format(case))
    qn = int(input())
    for q in range(qn):
        q = int(input())
        closest = arr[0] + arr[1]
        ab = abs(q - closest)
        for i in range(len(arr)):
            for j in arr[i + 1:]:
                s = arr[i] + j
                abx = abs(q - s)
                if abx < ab:
                    ab = abx
                    closest = s
        print("Closest sum to {} is {}.".format(q,closest))
    case += 1

tcase = int(input())

for case in range(tcase):
    gcm, lcm = map(int, input().split())
    if (lcm % gcm) == 0:
        print(gcm,lcm)
    else:
        print("-1")

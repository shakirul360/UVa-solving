min_steps = 0
tcase = int(input())
for case in range(tcase):
    x, y = map(int,input().split())
    difference = y - x
    min_steps = 0
    if difference != 0:
        sum_of_steps = 0
        z = 2
        while difference > sum_of_steps:
            sum_of_steps += z // 2
            min_steps += 1
            z += 1
    print(min_steps)

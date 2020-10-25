tcase = 1
while True:
    devices, operations, capacity = map(int, input().split())
    if devices == 0 and operations == 0 and capacity == 0:
        break
    devs = [0]
    devs_bool = [False for d in range(devices + 1)]
    highest = 0
    top = 0
    blown = False
    for i in range(devices):
        dv = int(input())
        devs.append(dv)
    for op in range(operations):
        operation = int(input())
        if devs_bool[operation] == False:
            highest += devs[operation]
            devs_bool[operation] = True
            if top < highest:
                top = highest
        else:
            highest -= devs[operation]
            devs_bool[operation] = False
        if highest > capacity:
            blown = True
        
    print("Sequence {}".format(tcase))
    if blown:
        print("Fuse was blown.")
    else:
        print("Fuse was not blown.")
        print("Maximal power consumption was {} amperes.".format(top))
    tcase += 1
    print("")

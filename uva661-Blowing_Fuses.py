tcase = 1
while True:
    devices, operations, capacity = map(int,input().split())
    if devices == 0 and operations == 0 and capacity == 0:
        break
    devs = [0]
    dev_bool = [False for i in range(devices + 1)]
    blown = False
    for device in range(devices):
        dv = int(input())
        devs.append(dv)
    top = 0
    highest = 0
    for ope in range(operations):
        #print(highest)
        operation  = int(input())
        if dev_bool[operation] == False:
            highest += devs[operation]
            dev_bool[operation] = True
            if top < highest:
                top = highest
        else:
            dev_bool[operation] = False
            highest -= devs[operation]
        if highest > capacity:
            blown = True
            break
    print("Sequence {}".format(tcase))
    if blown == True:
        print("Fuse was blown.")
    else:
        print("Fuse was not blown.")
        print("Maximal power consumption was {} amperes.".format(top))
    tcase += 1
    print("")

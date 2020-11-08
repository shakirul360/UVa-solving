tcase = int(input())
for case in range(tcase):
    blank = input()
    index = list(map(int,input().split()))
    xpi = [0 for i in range(len(index))]
    strings = list(input().split())
    #print(xpi)
    for idx in range(len(index)):
        #xpi.insert(index[idx], strings[idx])
        xpi[index[idx] - 1] = strings[idx]
    
    for j in xpi:
        print(j)
    if case == tcase -1:
        pass
    else:
        print("")

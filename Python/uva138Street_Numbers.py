house = [6, 35]
lastnum = [8, 49]

for i in range(8):
    last = 0
    seclast = house[-1]
    numlast = lastnum[-1]
    #print(seclast)
    h = 6 * house[-1] - house[-2]
    house.append(h)
    #print(house)
    last = h + seclast + numlast
    lastnum.append(last)
#print(house)
#print(lastnum)

for i in range(10):
    x = str(house[i])
    y = str(lastnum[i])
    #print(house[i], lastnum[i])
    print(x.rjust(10), end = '')
    print(y.rjust(10))

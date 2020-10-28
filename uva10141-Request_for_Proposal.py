def RFP(proposals):
    highest = 0
    brand = None
    price = None
    for prop in proposals:
        mets = int(proposals[prop][1])
    #print(x)
        if mets > highest:
            highest = mets
            brand = prop
            price = proposals[prop][0]
        if mets == highest:
            if proposals[prop][0] < price:
                price = proposals[prop][0]
                brand = prop    
    print(brand)

keep = []
while True:
    req_num, prop_num = map(int,input().split())
    if req_num == 0 and prop_num == 0:
        break
    proposals = {}
    for req in range(req_num):
        input()
    for prop in range(prop_num):
        name = input()
        proposals[name] = list()
        price_and_mets = list(map(float,input().split()))
        mets = int(price_and_mets[-1])
        proposals[name].extend(price_and_mets)
        for reqs in range(mets):
            req = input()
            proposals[name].append(req)
        
    keep.append(proposals)

for i in keep:
    print("RFP #{}".format(keep.index(i) + 1))
    if i == keep[-1]:
        RFP(i)
    else:
        RFP(i)
        print("")

n=int(input())
for i in range(n):
    l = int(input())
    train_order = []
    for j in range(l):
        num = int(input())
        train_order.append(num)
        count = 0
    for t in range(len(train_order) - 1):    
        for train in range(len(train_order) - 1): 
            if train_order[train + 1] < train_order[train]:
                train_order[train + 1],train_order[train] = train_order[train],train_order[train + 1]
                count += 1
            else:
                pass    
    print("Optimal train swapping takes {} swaps.".format(count))

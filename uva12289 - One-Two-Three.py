one = ["o","n","e"]
two = ["t", "w","o"]
tcase = int(input())
for case in range(tcase):
    arr = list(map(str,input()))
    oneb = []
    count = 0
    if len(arr) > 3:
        print("3")
    else:
        for i in arr:
                if str(i) in one:
                    if str(i) in oneb:
                        pass
                    else:
                        count += 1
                        oneb.append(str(i))
                    #print(count)
        if count >= 2:
            print("1")
        else:
            print("2")
        

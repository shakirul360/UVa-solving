import statistics 

arr = []
while True:
    try:
        n = int(input())
    except:
        break
    arr.append(n)
    arr = sorted(arr)
    med = str(statistics.median(arr))
    x = list(med.split("."))
    print(x[0])
    #print(med)
    
    

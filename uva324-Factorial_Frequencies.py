arr = [1, 1]

for i in range(2,367):
    res = arr[i - 1] * i
    arr.append(res)

while True:
    catalog = {"0": 0, "1": 0, "2" : 0, "3" : 0, "4": 0, "5" : 0, "6": 0, "7": 0, "8": 0, "9": 0}
    n = int(input())
    if n == 0:
        break
    string = str(arr[n])
    for i in string:
        catalog[i] += 1
    
    print("{}! --".format(n))
    print("   (0)  {}    (1)   {}    (2)   {}    (3)   {}    (4)   {}\n   (5)  {}    (6)   {}    (7)   {}    (8)   {}    (9)   {}".format(catalog["0"], catalog["1"], catalog["2"], catalog["3"], catalog["4"], catalog["5"], 
                                                                                                                                       catalog["6"], catalog["7"], catalog["8"], catalog["9"]))

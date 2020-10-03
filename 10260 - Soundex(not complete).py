catalog = {"B" : 1, "F": 1, "P": 1, "V" : 1,
           "C" : 2, "G" : 2, "J" : 2, "K" : 2, "Q" : 2, "S" : 2, "X": 2, "Z" : 2,
           "D" : 3, "T" : 3, "L" : 4, "M" : 5 , "N" :5, "R" : 6}


while True:
    res_string = ''
    string = []
    inp = input()
    for _ in inp:
        string.append(_)
    try:
        for i in range(len(string)):
            x = string[i]
    #y = string[i + 1]
            if x in catalog:
                res_string += str(catalog[x])
                if y in catalog:
                    try:
                        string.pop(i + 1)
                    except:
                        pass
    except:
        pass
    
        print(res_string)

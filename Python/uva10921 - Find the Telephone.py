while True:
    try:
        string = input()
    except EOFError:
        break
    arr = []
    for i in string:
        if i == "A" or i == "B" or i == "C":
            arr.append(2)
        elif i == "D" or i == "E" or i == "F": 
            arr.append(3)
        elif i == "G" or i == "H" or i == "I":
            arr.append(4)
        elif i == "J" or i == "K" or i == "L":
            arr.append(5)
        elif i == "M" or i == "N" or i == "O":
            arr.append(6)
        elif i == "P" or i == "Q" or i == "R" or i == "S":
            arr.append(7)
        elif i == "T" or i == "U" or i == "V":
            arr.append(8)
        elif i == "W" or i == "X" or i == "Y" or i == "Z":
            arr.append(9)
        else:
            arr.append(i)
    fin_string = ''.join([str(z) for z in arr])
    print(fin_string)
    
        

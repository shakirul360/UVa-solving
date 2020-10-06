while True:
    inp = input()
    if inp == "0":
        break
    
    n, string = inp.split()
    x = len(string) // int(n)
    arr = []
    for i in range(x - 1, len(string), x):
        for j in range(x):
            arr.append(string[i-j])
    print("".join(arr))

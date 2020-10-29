def mazes(arr):
    i = 0
    for i in arr:
        #print(i)
        num = list(i[::2])
        alph = list(i[1::2])
        res = ''
        for a in range(len(alph)):
            if alph[a] != "b":
                res = res + (alph[a] * int(num[a]))
            else:
                res = res + (" " * int(num[a]))
        print(res)
    
while True:
    string = input()
    arr = list(string.split("!"))
    mazes(arr)
    
    
# Wrong approach taken. every alphabet's previous numbers represent how many times an alphabet will be printed. if 21 beforex, print 3x

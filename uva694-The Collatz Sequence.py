case = 1
while True:
    a , l = map(int,input().split())
    x = a
    if a < 0 and l < 0:
        break
    count = 0
    while a <= l:
        #print(a)
        if a == 1:
            count += 1
            break
        elif a % 2 == 0:
            a = a // 2 
            count += 1
        elif a % 2  != 0:
            a = 3 * a + 1
            count += 1
    print("Case {}: A = {}, limit = {}, number of terms = {}".format(case,x,l,count))
    case += 1

from math import gcd

def divine(n1, n2):
    
    n1 = int(bin(n1)[2:])
    n2 = int(bin(n2)[2:])
    
    str1count1, str1count0 = 0, 0
    
    while n1 != 0:
        if n1 % 10 == 0:
            str1count0 += 1
        else:
            str1count1 += 1
        
        n1 = n1 // 10
                
    #-------------------\n    
    str2count1, str2count0 = 0, 0
    while n2 != 0:
        if n2 % 10 == 0:
            str2count0 += 1
        else:
            str2count1 += 1
        
        n2 = n2 // 10
                
                
    x = gcd(str1count1, str1count0)
    y = gcd(str2count1, str2count0)
    if (x == y and x == 1):
        return 1
    else:
        return 0
                
tcase = int(input())
for x in range(tcase):
    a, b = input().split()
    a = int(a)
    b = int(b)
    count = 0
    for i in range(a, b):
        for j in range(i + 1, b + 1):
            res = divine(i,j)
            if res == 1:
                count += 1
    
    print(count)
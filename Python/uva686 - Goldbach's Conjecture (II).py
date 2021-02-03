def Sieve(n): 
    prime = [True for i in range(n+1)] 
    p = 2
    while (p * p <= n): 
        if (prime[p] == True): 
            for i in range(p * p, n+1, p): 
                prime[i] = False
        p += 1
    arr = []
    for p in range(2, n+1): 
        if prime[p]: 
            arr.append(p)
#___________________________________________________Till this line is the process of Sieve________________________________________###
    arr2 = []
    for i in arr:
        a, b = i, n - i
        if b in arr:
            nums = [a,b]
            if nums in arr2 or nums[::-1] in arr2:
                pass
            else:
                arr2.append(nums)
    print(len(arr2))
    
while True:
    n = int(input())
    if not n:
        break
    Sieve(n)

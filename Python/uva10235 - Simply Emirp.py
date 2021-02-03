arr = []
def Sieve(n): 
    prime = [True for i in range(n+1)] 
    p = 2
    while (p * p <= n): 
        if (prime[p] == True): 
            for i in range(p * p, n+1, p): 
                prime[i] = False
        p += 1
    for p in range(2, n+1): 
        if prime[p]: 
            arr.append(p)
            
while True:
    try:
        n1 = int(input())
    except EOFError:
        break
    n2 = ''
    for i in reversed(str(n1)):
        n2 += i
        
    n2 = int(n2)
    if  n1 > n2:
        Sieve(n1)
    else:
        Sieve(n2)
    
    if n1 not in arr:
        print("{} is not prime.".format(n1))    
    else:
        if n2 in arr:
            print("{} is emirp.".format(n1))
        else:
            print("{} is prime.".format(n1))

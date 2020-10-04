import random 

def sieve(n):
    prime = [True for i in range(n + 1)]
    p = 2
    while (p * p <= n):
        if prime[p] == True:
            for i in range(p * p, n + 1, p):
                prime[i]= False
        p += 1
        arr = []
    for i in range(2,n + 1):
        if prime[i] == True:
            arr.append(i)
    return arr

def fermat(n):
    for i in range(5):
        a = random.randint(2, n - 1)
        if (pow(a, n) % n ) == a:
            result = True
        else:
            result = False
            return result
    return result

while True:
    n = int(input())
    if n == 0:
        break
    arr = sieve(n)
    if fermat(n) == True and  n in arr[::-1]:
        print("{} is normal.".format(n))
    else:
        print("The number {} is a Carmichael number.".format(n))

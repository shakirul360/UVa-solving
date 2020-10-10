def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            if i not in factors:
                factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

while True:
    n = int(input())
    if n == 0:
        break
    else:
        print("{} : {}".format(n,len(prime_factors(n))))

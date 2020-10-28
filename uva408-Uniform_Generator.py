from math import gcd
while True:
    try:
        step, mod = map(int,input().split())
    except EOFError:
        break
    x = 0
    if gcd(step, mod) == 1:
        print('{:>10}{:>10}    Good Choice'.format(step, mod))
    else:
        print('{:>10}{:>10}    Bad Choice'.format(step, mod))
    print("")

import operator as op
from functools import reduce

def ncr(n, r):
    r = min(r, n-r)
    # reduce passes in a function, op.mul (*), and iterates for all items on the passed on list.
    #op.mul is the multiply method.
    numer = reduce(op.mul, range(n, n-r, -1), 1)
    denom = reduce(op.mul, range(1, r+1), 1)
    return numer // denom 

while True:
    total, chosen = map(int,input().split())
    if total == 0 and chosen == 0:
        break
    print(ncr(total, chosen))

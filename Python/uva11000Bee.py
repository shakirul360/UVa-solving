mcat = {}
def male(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n >= 2:
        if (n - 1) in mcat and (n - 2) in mcat:
            a, b = mcat[n - 1], mcat[n - 2]
        elif (n - 1) in mcat and (n - 2) not in mcat:
            a = mcat[n - 1]
            b = male(n - 2)
            mcat[n - 2] = b
        elif (n - 1) not in mcat and (n - 2) in mcat:
            a = male(n - 1)
            mcat[n - 1] = a
            b = mcat[n - 2]
        else:
            a = male(n - 1)
            mcat[n - 1] = a
            b = male(n - 2)
            mcat[n - 2] = b
        return a + b + 1

def fmale(n):
    if n == 0:
        return 1
    elif n >= 1:
        if (n - 1) in mcat:
            return mcat[n - 1] + 1
        else:
            return male(n - 1) + 1

#print(male(3), fmale(3))

while True:
    n = int(input())
    if n == -1:
        break
    print(male(n), (fmale(n) + male(n)))
    #print(mcat)

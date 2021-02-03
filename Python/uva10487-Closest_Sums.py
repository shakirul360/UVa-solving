import sys
import itertools
import bisect

def fn(z): return sum(z)

w = 0
for s in sys.stdin:
    n = int(s)
    if(n == 0): break
    w += 1
    f = []
    for _ in range(n):
        f.append(int(sys.stdin.readline()))
    t = sorted(list(map(fn, itertools.combinations(f, 2))))
    m = int(sys.stdin.readline())
    print('Case {}:'.format(w))
    #print(t)
    gh = len(t)
    for _ in range(m):
        h = int(sys.stdin.readline())
        v = bisect.bisect_left(t, h)
        r = 0
        #print(v)
        if(v == gh): r = t[-1]
        elif(v == 0): r = t[0]
        else:
            r1, r2 = t[v], t[v-1]
            if(abs(r1-h) > abs(r2-h)):
                r = r2
            else:
                r = r1
        print('Closest sum to {} is {}.'.format(h, r))

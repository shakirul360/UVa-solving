from math import exp, sin, cos, tan
def solve(p,q,r,s,t,u):
    s1 = p*(exp(0))+q*sin(0)+r*cos(0)+s*tan(0)+t*0+u
    s2 = p*(exp(-1))+q*sin(1)+r*cos(1)+s*tan(1)+t*1+u
    
    if (s1 * s2 > 0):
        print("No solution")
        pass
    else:
        left, right = 0.0, 1.00
        while (right - left > 1e-9):
            mid = (left + right) / 2
            tmp = p * (exp (-mid)) + q * sin (mid) + r * cos (mid) + s * tan (mid) + t * mid * mid + u
            if (tmp <0):
                right = mid
            else:
                left = mid
                
        #print({'%4f'},format(mid))
        print("{:.4f}".format(mid))
        
while True:
    try:
        p, q, r, s, t, u = map(float,input().split())
    except EOFError:
        break
    solve(p,q,r,s,t,u)

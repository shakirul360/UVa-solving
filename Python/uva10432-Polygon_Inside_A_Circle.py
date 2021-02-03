import math
from math import radians, sin
while True:
    try:
        r, n = map(float,input().split())
        area = n * 0.5 * pow(r,2) * sin(math.radians(360 / n)) 
        print("{:.3f}".format(area))
    except EOFError:
        break
    

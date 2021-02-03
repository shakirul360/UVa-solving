from math import floor, ceil, sqrt

while True:
    a, b = map(int,input().split())
    total = 0
    if a == 0 and b == 0:
        break
    res = floor(sqrt(b)) - ceil(sqrt(a)) + 1
	print(res)

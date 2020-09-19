import sys

lines = list(sys.stdin().splitlines())
for i in lines:
    for j in i:
        x = chr(ord(j) - 7)
        print(x, end = '')

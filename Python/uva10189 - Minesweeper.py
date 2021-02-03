import sys
from itertools import *

data = sys.stdin.read().splitlines()

fields = []
import re
for i in range(0,len(data)):
    match = re.match('(\d+) (\d+)', data[i])
    if match:
        r = int(match.group(1))
        if r != 0:
            fields.append(data[i+1 : i+1+r])

for field in fields:
    for (x,y) in product(range(len(field)), range(len(field[0]))):

        if field[x][y] == '*':
            continue

        count = 0
        for (x_offset, y_offset) in product(range(-1,2), repeat=2):

            if x_offset == y_offset == 0 or x+x_offset < 0 or y_offset+y < 0:
                continue

            try:
                if field[x+x_offset][y+y_offset] == '*':
                    count += 1
            except IndexError:
                pass

        row = list(field[x])
        row[y] = str(count)
        field[x] = ''.join(row)

for i in range(0,len(fields)):
    print("Field #%i:" % (i+1))
    for row in fields[i]:
        print(row)

    if i < len(fields)-1:
        print()


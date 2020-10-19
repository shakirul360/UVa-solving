import math
import itertools

while True:
    count = 0
    n = int(input())
    if n == 0:
        break
    numbers = []
    for num in range(n):
        numbers.append(input())
    perms = (list(itertools.combinations(numbers, 2)))
    for i in perms:
                  if math.gcd(int(i[0]),int(i[1])) == 1:
                      count +=1
    if count == 0:
        print("No estimate for this data set.")
    else:
        x = len(perms)
        res = math.sqrt(len(perms)/ count * 6)
        print(format(res, '.6f'))

carmichael = [561, 1105, 1729, 2465, 2821, 6601, 8911, 10585, 15841, 29341, 41041, 46657, 52633, 62745,  63973]

while True:
    n = int(input())
    if n == 0:
        break
    if n in carmichael:
        print("The number {} is a Carmichael number.".format(n))
    else:
        print("{} is normal.".format(n))

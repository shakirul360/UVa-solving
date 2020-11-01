fibs = [0,1]
for i in range(2,5001):
    x = fibs[-1] + fibs[-2]
    fibs.append(x)
    

while  True:
    try:
        n = int(input())
    except EOFError:
        break
    print("The Fibonacci number for {} is {}".format(n, fibs[n]))

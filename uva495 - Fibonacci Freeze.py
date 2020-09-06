import math
while True:
    try:
        n = int(input())
        fib = ((pow(1.618034, n)- pow((1-1.618034),n)) / math.sqrt(5))
        print("The  Fibonacci  number  for  {}  is  {}".format(n,round(fib)))
        print(fib)
    except:
        break

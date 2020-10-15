from math import factorial

while True:
    try:
        n = int(input())
    except EOFError:
        break
    if n > 0:
        if n <= 7:
            print("Underflow!")
        elif n >= 14:
            print("Overflow!")
        else:
            print(factorial(n))
    else:
        if n % 2 == 0:
            print("Underflow!")
        else:
            print("Overflow!")

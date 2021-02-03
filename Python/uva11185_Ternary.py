while True:
    n = int(input())
    if n < 0:
        break
    
    remainder = ''
    if n == 0:
        remainder = 0
        
    while n > 0:
        remainder = str(n % 3) + remainder
        n //= 3
    
    print(remainder)

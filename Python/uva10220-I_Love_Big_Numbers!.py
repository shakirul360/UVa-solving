arr = [1,1]
for i in range(2,1001):
    res = arr[-1] * i
    arr.append(res)
    
def sum_digits(n):
    s = 0
    while n:
        s += n % 10
        #print(s)
        n //= 10
    return s

while True:
    try:
        n = int(input())
    except EOFError:
        break
    x = arr[n]
    print(sum_digits(x))

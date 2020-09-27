factorial = [1]*601
a = 1
for i in range(1,600+1):
    a*=i 
    factorial[i] = a
    
while True:
    n = int(input())
    if  n == 0:
        break
    res = factorial[n * 2] // factorial[n + 1]
    print(res)

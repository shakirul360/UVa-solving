factorial = [1]*1001
a = 1
for i in range(1,1000+1):
    a*=i 
    factorial[i] = a
    
while True:
    try:
        n = int(input())
    except EOFError:
        break
    print("{}!".format(n))
    print(factorial[n])

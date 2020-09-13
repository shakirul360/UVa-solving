def prime(num):
    if num == 0:
        return False
    if num == 1:
        return False
    for i in range(2,num):
        if (num % i) == 0:
            return False
    else:
        return True
    
while True:
    n = int(input())
    if n == 0:
        break
    count = 0
    arr = []
    for j in range(2,n):
        if prime(j) == True:
            a = j
            b = n - j
            if prime(b) == True:
                count += 1
                num = [a,b]
                if num in arr or num[::-1] in arr:
                    pass
                else:
                    arr.append(num)
    print(len(arr))

n = int(input())
for _ in range(n):
    n,m = map(int,input().split())    
    result = (n//3) * (m//3)
    print(result)

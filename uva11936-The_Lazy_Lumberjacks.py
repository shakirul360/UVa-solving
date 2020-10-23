def checkValidity(a, b, c):  
    if (a + b <= c) or (a + c <= b) or (b + c <= a) : 
        return False
    else: 
        return True        
  
# driver code  
tcase = int(input())
for case in range(tcase):
    a,b,c= map(int,input().split())
    if checkValidity(a, b, c): 
        print("OK")  
    else: 
        print("Wrong!!") 

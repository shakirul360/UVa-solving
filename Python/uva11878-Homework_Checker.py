count=0
while True:
    try:
        s=input()
        result=s.split('=')
        if result[0].find('+')>0:
            a,b=result[0].split('+')
            a=int(a)
            b=int(b)
            
            if result[1]!='?' and a+b==int(result[1]):
                count+=1
           
        else:
            a,b=result[0].split('-')
            a=int(a)
            b=int(b)
           
            if  result[1]!='?' and a-b==int(result[1]):
                count+=1
            
    except EOFError:
        print(count)
        break

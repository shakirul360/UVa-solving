while True:
    try:
        x = int(input())
    except EOFError:
        break
    ans = 1
    ans=ans*x*(x+1)//2
    ans=ans*x*(x+1)//2;
    print(ans)

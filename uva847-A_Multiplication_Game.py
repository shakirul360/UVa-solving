while True:
    try:
        n = int(input())
    except EOFError:
        break
    p = 1
    i = 1
    while True:
        if i % 2 == 1:
            p = p * 9
        else:
            p = p * 2
    
        if p >= n:
            break
        i += 1
    
    if i % 2 == 1:
        print("Stan wins.")
    else:
        print("Ollie wins.")

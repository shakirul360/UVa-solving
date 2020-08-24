while True:
    try:
        a, b = input().split()
    except EOFError:
        break
    # The lines below turns an integer to a 32-bit binary list
    dec_a = list('{:032b}'.format(int(a)))
    dec_b = list('{:032b}'.format(int(b)))
    #print(dec_a,dec_b)
    dec_c = []
    for i in range(min(len(dec_a), len(dec_b))):
        if dec_a[i]  != dec_b[i]:
            dec_c.append(1)
        else:
            dec_c.append(0)
    # The line below joins the dec_c items to fin_dec
    fin_dec = ''.join([str(_) for _ in dec_c])
    #The line below turns the 32-bit binary to decimal
    print(int(fin_dec,2))
    
    
    

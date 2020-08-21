while True:
    h, u, d, f = [int(x) for x in input().split()]
    if h == 0:
        break
    fat = u * f / 100
    climb = 0
    day = 1
    while True:
        if u > 0:
            climb = climb + u
        u -= fat
        if climb > h:
            r = 'success'
            break
        climb -= d
        if climb < 0:
            r = 'failure'
            break
        day += 1
    print('{} on day {}'.format(r, day))
        

    
    
   
    

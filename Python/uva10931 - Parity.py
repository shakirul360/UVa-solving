while True:
    n = int(input())
    if not n:
        break
    par = bin(n)
    count = 0
    for i in par:
        if i == "1":
            count += 1
    print("The parity of {} is {} (mod 2).".format(par[2::],count))

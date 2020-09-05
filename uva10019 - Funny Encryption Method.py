tcases = int(input())
for i in range(tcases):
    count1 = 0
    count2 = 0
    n = int(input())
    bin_n = bin(n)
    for x in bin_n:
        if x == "1":
            count1 += 1
    z = int('0x{}'.format(n), 16)
    for i in bin(z):
        if i == "1":
            count2 += 1
    print(count1,count2)

def mile(sec):
    return (sec // 30) * 10 + 10
    
def juice(sec):
    return (sec // 60) * 15 + 15

tcase = int(input())
for case in range(tcase):
    ints = int(input())
    mprice, jprice = 0, 0
    arr = list(map(int,input().split()))
    for num in arr:
        mprice += mile(num)
        jprice += juice(num)
    
    if mprice < jprice:
        print("Case {}: Mile {}".format(case + 1, mprice))
    elif jprice < mprice:
        print("Case {}: Juice {}".format(case + 1, jprice))
    else:
        print("Case {}: Mile Juice {}".format(case + 1, mprice))

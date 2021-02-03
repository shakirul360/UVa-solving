two = ["00", "01", '81']
four = ['0000', '0001','2025', '3025', '9801']
six = ['000000','000001','088209','494209', '998001']
eight = ['00000000','00000001','04941729','07441984','24502500','25502500','52881984','60481729','99980001']

while True:
    try:
        n = int(input())
    except EOFError:
        break
    if n == 2:
        for i in two:
            print(i)
    elif n == 4:
        for i in four:
            print(i)
    elif n == 6:
        for i in six:
            print(i)
    else:
        for i in eight:
            print(i)

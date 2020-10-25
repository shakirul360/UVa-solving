tcase = int(input())
x = input()
for case in range(tcase):
    length = int(input())
    num1 = ''
    num2 = ''
    for l in range(length):
        n1, n2 = input().split()
        num1 += n1
        num2 += n2
    if case != (tcase - 1):
        z = input()
    res = int(num1) + int(num2)
    print(res)
    print("")

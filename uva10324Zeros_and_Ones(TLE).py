count = 1
while True:
    try:
        string = input()
    except EOFError:
        break
    if string == '':
        break
    print("Case {}:".format(count))
    count += 1
    tcase =int(input())
    for case in range(tcase):
        a, b = map(int,input().split())
        if a > b:
            b, a = a, b
        yes_or_no = "No"
        check = string[b]
        for num  in string[a : (b + 1)]:
            if num != check:
                yes_or_no = "No"
                break
            else:
                yes_or_no = "Yes"
        print(yes_or_no)

tcase = int(input())
for case in range(tcase):
    string = input()
    count = 0
    previous = 0
    for i in string:
        if i == "O":
            previous += 1
            count += previous
        else:
            previous = 0
        
    print(count)

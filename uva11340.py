tcase = int(input())
for i in range(tcase):
    dictionary = {}
    sum = 0.0
    k = int(input())
    for j in range(k):
        letter, price = input().split()
        dictionary[letter] = int(price)
    string_num = int(input())
    s = ''
    for _ in range(string_num):
        string = input()
        for let in string:
            if let in dictionary:
                sum += dictionary[let]
                
    print('%0.2f$' %(sum/100.0))

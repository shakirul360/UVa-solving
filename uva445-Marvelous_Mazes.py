from string import ascii_uppercase

def mazes(arr):
    letters = list(ascii_uppercase)
    letters.append('b')
    letters.append('*')
    res = []
    #1T1b5T!1T2b1T1b2T!1T1b1T2b2T!1T3b1T1b1T!3T3b1T!1T3b1T1b1T!5T1*1Tprint(letters)
    for substring in arr:
        res_string = ''
        sub_arr = [ch for ch in substring]
        while len(sub_arr) > 0:
            for let in sub_arr:
                #print(sub_arr)
                print_num = 0
                if let in letters or let == 'b':
                    if let == 'b':
                        let_idx = sub_arr.index(let)
                        for num in sub_arr[:let_idx]:
                            print_num += int(num)
                        res_string += " " * print_num
                    else:
                        let_idx = sub_arr.index(let)
                        for num in sub_arr[:let_idx]:
                            print_num += int(num)
                        res_string += let * print_num
                    for ch in sub_arr[:let_idx + 1]:
                        sub_arr.remove(ch)
                    break
        res.append(res_string)
                    
    for x in res:
        print(x)

while True:
    try:
        string = input()
    except EOFError:
        break
    arr = list(string.split("!"))
    mazes(arr)

dicts= {'a': 1,'b': 2,'c': 3,'d': 4,'e': 5,'f': 6,
        'g': 7,'h': 8,'i': 9,'j': 10,'k': 11,'l': 12,
        'm': 13,'n': 14,'o': 15,'p': 16,'q': 17,'r': 18,
        's': 19 ,'t': 20,'u': 21,'v': 22,'w': 23,'x': 24,'y': 25,'z': 26}

def string_val_calculator(string):
    sum1 = 0
    for i in string:
        let = i.lower()
        if let in dicts:
            sum1 += dicts[let]
    final_add1 = 0
    for s in str(sum1):
        final_add1 += int(s)
    return final_add1

while True:
    try:
        string1 = input()
        string2 = input()
    except EOFError:
        break

    a = string_val_calculator(string1)
    b = string_val_calculator(string2)

    print("The sum value of the word {} is {}".format(string1,a))
    print("The sum value of the word {} is {}".format(string2,b))

    if a > b:
        res = (b / a) * 100
    else:
        res = (a / b) * 100
    
    formatted_res = "{:.2f} %".format(res)
    print(formatted_res)

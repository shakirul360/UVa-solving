n = int(input())
for i in range(n):
    string = input()
    slen = len(string)
    if string == "1" or string == "4" or string == "78":
        print("+")
    elif string[slen-2: ] == "35":
        print("-")
    elif string[0] == "9" and string[slen - 1] == "4":
        print("*")
    elif string[0:3]=="190":
        print("?")
    else:
        print("?")
    

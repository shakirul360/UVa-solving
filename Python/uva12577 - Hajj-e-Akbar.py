#create an endless loop
#take input of string containing hajj or umrah or *
#if " * ", break
#else if hajj, print hajj - e -Akbar
#else print(hajj e Asghar)
n = 0

while True:
    str = input()
    n += 1
    if str == "*":
        break
    elif str == "Hajj":
        print("Case {:,}:".format(n),'Hajj-e-Akbar')
    elif str == "Umrah":
        print("Case {:,}:".format(n),'Hajj-e-Asghar')

dictionary = {}
while True:
    x = input()
    if x == "":
        break
    eng, fo = x.split()
    if fo not in dictionary:
        dictionary[fo] = eng
    else:
        pass

while True:
    try:
        query = input()
    except EOFError:
        break
    if query in dictionary:
        print(dictionary[query])
    else:
        print('eh')

while True:
    try:
        string = input()
    except EOFError:
        break
    for i in string:
        x = chr(ord(i) - 7)
        print(x, end = '')

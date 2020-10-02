punc = ['.', ',', '!', '?', " "]
while True:
    string = input().lower()
    if string == "done":
        break
    for i in string:
        if i in punc:
            string = string.replace(str(i), '')
        rev_string = string[::-1]
    #print(rev_string, string)
    if rev_string == string:
        print("You won't be eaten!")
    else:
        print("Uh oh..")

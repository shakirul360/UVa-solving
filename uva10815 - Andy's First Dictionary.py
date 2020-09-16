dictionary = []
while True:
    try:
        sentence = list(input().split(" "))
    except EOFError:
        for i in sorted(dictionary):
            print(i)    
    for i in sentence:
        a = i.lower()
        if a in dictionary:
            pass
        else:
            final_word = "".join(u for u in a if u not in ("?", ".", ";", ":", "!", '"'))
            dictionary.append(final_word)

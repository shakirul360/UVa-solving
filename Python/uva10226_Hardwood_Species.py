trees = {}

n = int(input())

for i in range(n):
    count = 0
    print(" ")
    while True:
        try:
            tree = input()
        except EOFError:
            break
        count += 1
        if tree in trees:
            trees[tree] += 1
        else:
            trees[tree] = 1
    for i in sorted (trees) : 
        print (i, "{0:.4f}".format(trees[i] / count * 100))
    print("")

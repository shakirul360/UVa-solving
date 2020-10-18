import itertools 

tcase = int(input())

for case in range(tcase):
    string = list(input())
    permutations = sorted(list(set(itertools.permutations(string))))
    #print(permutations)
    for permutation in permutations:
        print(''.join(permutation))
    print("")

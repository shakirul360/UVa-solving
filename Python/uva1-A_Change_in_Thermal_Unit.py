def cel_to_fahr(n):
    return ((9 / 5) * n) + 32

def fahr_to_cel(n):
    return ((n - 32) * 5) / 9

tcase = int(input())
for case in range(tcase):
    cels, fahr_increase = map(int,input().split())
    fahr = cel_to_fahr(cels)
    result = fahr_to_cel(fahr + fahr_increase)
    print("Case {}: {}".format(case +1, format(result, '.2f')))

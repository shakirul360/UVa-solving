from collections import Counter

def common_permutation(a, b):
    return ''.join(k * v for k, v in sorted((Counter(a) & Counter(b)).items()))

while(1):
    try:
        a = input()
        b = input()
    except EOFError:
        break
    print(common_permutation(a, b))

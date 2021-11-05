string1 = input()
string2 = input()
res = []
print(string1, string2)

len1 = len(string1)
len2 = len(string2)

try:
    fin = ''
    for i in range(len1):
        res.append(string1[i])
        res.append(string2[i])
    
except IndexError:
    pass

print(fin.join(res))
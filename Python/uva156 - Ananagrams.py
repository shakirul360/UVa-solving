from collections import Counter


list_raw = []
while True:
    _str = input()
    if _str == "#":
        break
    else:
        list_raw.extend(list(_str.split(' ')))
#print("This is the list_raw", list_raw)

def Lower(s_1):
    return s_1.lower()


def Sort(s_2):
    return ''.join(sorted(s_2))


def Find(s_3):
    if s_3[1] == 1:  # Check whether the subtitle group is unique, and the only one is to return the words in the original list according to the sorted alphabet group index
        return list_raw[list_sort.index(s_3[0])]


list_low = map(Lower, list_raw)
#print("list_low =", list_low)
list_sort = list(map(Sort, list_low))
#print("List_sort =", list_sort)
number = Counter(list_sort).items()
#print(number)
ana = list(filter(None, map(Find, number)))
#print(ana)
# The filter filters out None, because the word group is not unique, the word group function has no return value
for i in sorted(ana):
    print(i)


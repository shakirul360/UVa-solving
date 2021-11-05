string = input()

dictionary = {}

for i in string:
    if i not in dictionary:
        dictionary[i] = 1
    else:
        dictionary[i] += 1 
        

#print(dictionary)

res = " "
for i in dictionary:
    if dictionary[i] >= 2:
        for j in range(2):
            print(i, end = '')

#print("")

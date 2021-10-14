string = input()

dictionary = {}

for i in string:
    if i not in dictionary:
        dictionary[i] = 1
    else:
        dictionary[i] += 1 
        

#print(dictionary)

res = " "
found = 0

for i in dictionary:
    if dictionary[i] >= 2:
        found = 1
        for j in range(2):
            print(i, end = '')
    
    break

if found == 0:
    print("NO SOLUTION")

#print("")

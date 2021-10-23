dic1 = {}
dic2 = {}
flag = True

for i in range(2):
    string = input()
    for i in string:
        if i in dic1:
            dic1[i] += 1
        else:
            dic1[i] = 1

fin_string = input()
for j in fin_string:
    if j in dic2:
        dic2[j] += 1
    else:
        dic2[j] = 1

for i in dic1:
    if (i in dic2 and dic1[i] == dic2[i]):
        dic2[i] = 0
        flag = True
    else:
        flag = False
        break
        
for x in dic2:
    if dic2[x] > 0:
        flag = False
        break
        
if (flag == True):
    print("YES")
else:
    print("NO")
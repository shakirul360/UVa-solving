string = input()
n1,n2,n3 = 0,0,0
numbers = []
length = len(string)

for i in string:
    if i == '1' or i == '2' or i == '3':
        numbers.append(int(i))
        
numbers.sort()

for i in range(len(numbers)):
    print(numbers[i], end = '')
    if (length == 1 or i == len(numbers) - 1):
        break
    else:
        print('+', end = '')
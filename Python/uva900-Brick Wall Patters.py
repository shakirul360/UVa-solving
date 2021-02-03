values = [ 0 for i in range(55)]

values[1], values[2] = 1, 2
for i in range(3, 55):
    values [i] = values[i - 1] + values[i - 2]

while True:
    n = int(input())
    if not n:
        break
    print(values[n])

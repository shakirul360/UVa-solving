arr = [1, 1]
for i in range(2,10001):
    x = i * arr[i - 1]
    arr.append(x)

while True:
    try:
        n = int(input())
    except EOFError:
        break
    string = str(arr[n])
    z = string.rstrip('0')
    if n > 999: #four digits
        print(" {} -> {}".format(n, z[-1]))
    if n > 99 and n < 1000:
        print("  {} -> {}".format(n, z[-1]))
    if n > 9 and n < 99: #two digits
        print("   {} -> {}".format(n, z[-1]))
    if n < 10: # one digit
        print("    {} -> {}".format(n, z[-1]))

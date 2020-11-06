def depth(n,dep):
    summ = 0
    for digit in str(n):
        summ += int(digit)
    dep += 1
    if summ > 9:
        return depth(summ, dep)
    
    return summ, dep
    
#depth(n,dep)
while True:
    n = int(input())
    if n == 0:
        break
    dep = 0
    summ, dep = depth(n,dep)
    if summ == 9:
        print("{} is a multiple of 9 and has 9-degree {}.".format(n,dep))
    else:
        print("{} is not a multiple of 9.".format(n))

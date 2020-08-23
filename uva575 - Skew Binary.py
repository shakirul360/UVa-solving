import math

while True:
    nums = []
    integer = input()
    if integer == "0":
        break
    for i in integer:
        i = int(i)
        nums.append(i)
    leng = len(nums)
    total = 0
    y = leng
    for x in nums:
        skew = (x * (math.pow(2,y) - 1))
        total += skew
        y = y - 1
    print(int(total))

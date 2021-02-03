def numSquareSum(n): 
	squareSum = 0; 
	while(n): 
		squareSum += (n % 10) * (n % 10); 
		n = int(n / 10); 
	return squareSum

def isHappynumber(n): 
    slow = n 
    fast = n
    while(True):
        slow = numSquareSum(slow)  
        fast = numSquareSum(numSquareSum(fast)) 
        if(slow != fast): 
            continue 
        else: 
            break 
    return (slow == 1)

tcase = int(input())
for case in range(tcase):
    n = int(input())
    if isHappynumber(n) == True:
        print("Case #{}: {} is a Happy number.".format(case + 1, n))
    else:
        print("Case #{}: {} is an Unhappy number.".format(case + 1, n))

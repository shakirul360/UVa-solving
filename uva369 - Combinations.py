def nCr1(n, m):
	if m > n:
		return  0
	if m > n // 2:
		m = n - m
		
	res = 1
	for i in range(m):
		res *= ( n  - i )
		res //= ( i + 1 )
	return res

while True:
	n ,m = map(int, input().split())
	# dp = [[-1 for i in range(0, 105)] for i in range(0, 105)]
	if n == 0 and m == 0: break
	print("%d things taken %d at a time is %d exactly." %( n, m, nCr1(n, m) ))

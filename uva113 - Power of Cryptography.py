while True:
	try:
		m = int(input())
		n = int(input())
	except EOFError:
		break
		
	print(round(n ** (1 / m)))

   

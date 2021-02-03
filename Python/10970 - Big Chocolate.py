"""In the beginning we have one piece of chocolate.
At the end we want to have m n {\displaystyle mn} {\displaystyle mn} pieces.
Each cut divides one piece into two, thus the number of pieces increases by one. 
Thus we will need exactly m n − 1 {\displaystyle mn-1} {\displaystyle mn-1} cuts regardless of the way we cut the chocolate"""

while True:
    try:
        m , n = map(int,input().split())
    except:
        break
    if m == 1 and n == 1:
        print("0")
    else:
        print((m * n) - 1)

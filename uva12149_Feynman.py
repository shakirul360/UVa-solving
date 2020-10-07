while True:
    n = int(input())
    if not n:
        break
    else:
        res = (n*(n + 1)*(2*n + 1) // 6)
        print(res)
        
"""If n = 1, there is one 1-by-1 square. """
"""If n = 2, there is one 2-by-2 square and four 1-by-1 squares."""
"""If n = 3, there is one 3-by-3 square, four 2-by-2 squares and nine 1-by-1 squares."""

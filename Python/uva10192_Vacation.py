# Dynamic programming implementation of LCS problem 

# Returns length of LCS for X[0..m-1], Y[0..n-1] 
def lcs(X, Y, m, n): 
    L = [[0 for x in range(n+1)] for x in range(m+1)] 

    # Following steps build L[m+1][n+1] in bottom up fashion. Note 
    # that L[i][j] contains length of LCS of X[0..i-1] and Y[0..j-1] 
    for i in range(m+1): 
        for j in range(n+1): 
            if i == 0 or j == 0: 
                L[i][j] = 0
            elif X[i-1] == Y[j-1]: 
                L[i][j] = L[i-1][j-1] + 1
            else: 
                L[i][j] = max(L[i-1][j], L[i][j-1]) 

    index = L[m][n] 

    lcs = [""] * (index+1) 
    lcs[index] = "" 

    i = m 
    j = n 
    while i > 0 and j > 0: 
        if X[i-1] == Y[j-1]: 
            lcs[index-1] = X[i-1] 
            i-=1
            j-=1
            index-=1

        elif L[i-1][j] > L[i][j-1]: 
            i-=1
        else: 
            j-=1
    
    return len("".join(lcs))

# Driver program
case = 1
while True:
    X = input()
    if X == '#':
        break
    Y = input()
    m = len(X) 
    n = len(Y)
    print("Case #{}: you can visit at most {} cities.".format(case, lcs(X, Y, m, n))) 
    case += 1

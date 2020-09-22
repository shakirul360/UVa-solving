first = True
while True:
    IN = list(map(int, input().split()))
    N, IN = IN[0], IN[1:]
    if N == 0:
        break
    if not first:
        print('')
    first = False
    for i in range(N):
        for j in range(i + 1, N):
            for k in range(j + 1, N):
                for l in range(k + 1, N):
                    for m in range(l + 1, N):
                        for n in range(m + 1, N):
                            print(str(IN[i]) + ' ' + str(IN[j]) + ' ' + str(IN[k]) +
                                  ' ' + str(IN[l]) + ' ' + str(IN[m]) + ' ' + str(IN[n]))

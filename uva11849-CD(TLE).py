import numpy

while True:
    n, m = map(int,input().split())
    if n == 0 and m == 0:
        break
    arr = []
    for i in range(n + m):
        arr.append(input())
    print(len(arr) - len(numpy.unique(arr)))


### A few more approaches were tried, but still facing TLE. Another code try below #####
#import time

#while True:
#   arr = []
#    n,m = map(int,input().split())
#    if n == 0 and m == 0:
#        break
#    for i in range(n + m):
#        arr.append(input())
#    start_time = time.time()
#
#    count = 0
#    for i in arr:
#        x = arr.remove(i)
#        if i in arr:
#            count += 1
#
#    print(count)
#    end_time = time.time()
#    print("Run time = {}".format(end_time - start_time))

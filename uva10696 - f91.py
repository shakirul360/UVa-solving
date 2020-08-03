cache = dict()

def f91(n: int) -> int:
    if n > 100:
        return n - 10
    else:
        if n in cache:
            return cache[n]
        else:
            result = f91(f91(n + 11))
            cache[n] = result
            return result
      
while True:
    n = int(input())
    if n == 0:
        break
    else:
        #f91(n)
        print("f91({}) = {}".format(n,f91(n)))
        #print(cache)

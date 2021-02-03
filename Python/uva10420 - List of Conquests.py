10420 - List of Conquests



countries = {}
n = int(input())
for i in range(n):
    arr = list(input().split())
    if arr[0] in countries:
        countries[str(arr[0])] += 1
    else:
        countries[str(arr[0])] = 1
        
for key,value in sorted(countries.items()):
    print(key,value)

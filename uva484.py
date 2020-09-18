dictonary = dict()
input_list=list()
while True:
  try:
    input_list = [x for x in map(int,input().split())]
    #print(input_list)
    for i in input_list:
      if i not in dictonary:
        dictonary[i]=1

      else:
        dictonary[i] += 1
  except EOFError:
    #print(dictonary)
    for i in dictonary:
        print(i, dictonary[i])
    break

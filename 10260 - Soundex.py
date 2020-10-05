catalog = {"B" : 1, "F": 1, "P": 1, "V" : 1,
           "C" : 2, "G" : 2, "J" : 2, "K" : 2, "Q" : 2, "S" : 2, "X": 2, "Z" : 2,
           "D" : 3, "T" : 3, "L" : 4, "M" : 5 , "N" :5, "R" : 6}

def remove_adjacent(nums):
     return [a for a,b in zip(nums, nums[1:]+[not nums[-1]]) if a != b]
    
while True:
    arr = []
    try:
        string = input()
    except EOFError:
        break
        
    for i in string:
        if i in catalog:
            arr.append(catalog[i])
        else:
            arr.append(0)
            
    arr = remove_adjacent(arr)
    
    res_string = ''
    for i in arr:
        if i > 0:
            res_string += str(i)
            
    print(res_string)

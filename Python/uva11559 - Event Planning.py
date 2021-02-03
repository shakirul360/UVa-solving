#create an endless loop
# take input of an array to get
# set minimum = -500000
# - n = number of participants
# - b = budget 
# - h = hotels
# - weeks to choose from
#then loop over range of hotels to get input of budget and weeks to choose from
# check if any week has open beds => n, if so,check if total > budget, total = budget * n, set it to total
# print("stay home")
_____________________________________________________________________________________________________________________

while True:
    try:
        n, b, h, w = map(int,input().split())
    except:
        break
    total = 0
    b1 = False
    for i in range(h):
        bed_price = int(input())
        empty_beds = list(map(int,input().split()))
        if (bed_price * n) <= b:
            empty_beds.sort(reverse=True)
            if empty_beds [0] >= n:
                    b1=True
                    if total == 0:
                        total =bed_price * n
                    elif bed_price * n < total:
                        total = bed_price * n
    
    if b1 :
        print(total)
    else:
        print("stay home")

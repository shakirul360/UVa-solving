def year_type(year):
    leap_bool = False
    flag = 0
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        print("This is leap year.")
        leap_bool = True
        flag = 1
    if year % 15 == 0:
        print("This is huluculu festival year.")
        flag = 1
    if year % 55 == 0 and leap_bool == True:
        print("This is bulukulu festival year.")
    if flag == 0:
        print("This is an ordinary year.")

#year_type(2000)
#year_type(3600)
#year_type(4515)
#year_type(2001)
arr = []
while True:
    try:
        year = int(input())
        arr.append(year)
    except EOFError:
        for y in range(len(arr)):
            if y != (len(arr) - 1):
                year_type(arr[y])
                print("")
            else:
                year_type(arr[y])
        break

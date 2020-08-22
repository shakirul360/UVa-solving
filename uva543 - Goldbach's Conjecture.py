while True:
    n = int(input())
    if n == 0:
        break
    arr = []
    for i in range(2,n): 
        for j in range(2,i): 
            if(i % j==0): 
                break
        else: 
            arr.append(i)
    numbers = arr
    target_number = n

    for i, number in enumerate(numbers[:-1]):  # note 1
        complementary = target_number - number
        if complementary in numbers[i+1:]:  # note 2
            print("{} = {} + {}".format(n,number, complementary))
            break
    else:  # note 3
        print("Goldbach's conjecture is wrong.")



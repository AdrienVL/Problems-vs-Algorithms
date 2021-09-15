def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    #Recursion - divide 16 / 2 = 8, 8 /2 = 4

    #O(N)

    # if number == 0:
    #     return 0

    # i = 1
    # while True:
    #     print(round(number/i))
    #     if round(number/i) == i:
    #         break
    #     i+=1
    


    # return i

    if number == 0:
        return 0

    current = round(number/2)

    while True:
        if current * current > number:
            current = round(current/2)
        elif current * current < number:
            current +=1
            break
        else:
            break
    return current

    # i = 1
    # while True:
    #     print(round(number/i))
    #     if round(number/i) == i:
    #         break
    #     i+=1
    

    # return i


print(sqrt(27))
# print ("Pass" if  (3 == sqrt(9)) else "Fail")
# print ("Pass" if  (0 == sqrt(0)) else "Fail")
# print ("Pass" if  (4 == sqrt(16)) else "Fail")
# print ("Pass" if  (1 == sqrt(1)) else "Fail")
# print ("Pass" if  (5 == sqrt(27)) else "Fail")

27

14
7
4
5


32
16
8
4
5


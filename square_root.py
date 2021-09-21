
#Achieve O(log(n)) using binary search
def sqrt(number):

    start_index = 0                                     #Range between 0 and number
    end_index = number
    
    while start_index <= end_index:
        mid_index = (start_index + end_index)//2        # integer division
        mid_number = mid_index
        
        if number == mid_number**2:                       # Returns perfect square root
            return mid_index
        
        elif number < mid_number**2:                      # the target is less than mid element
            end_index = mid_index - 1                   # we will only search in the left half
        
        else:                                           # the target is greater than mid element
            start_index = mid_number + 1               # we will search only in the right half
    
    return mid_index                                   #Returns floored square root




print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")







import timeit

start = timeit.default_timer()


import time
import matplotlib.pyplot as plt

x_coordinate = []
y_coordinate = []

array = list(range(1000))
start = time.time()

    

def sqrt(number):

    start_index = 0
    end_index = number
    
    while start_index <= end_index:
        mid_index = (start_index + end_index)//2        # integer division in Python 3
        print(mid_index)
        mid_element = mid_index
        
        if number == mid_element**2:                       # we have found the element
            return mid_index
        
        elif number < mid_element**2:                      # the target is less than mid element
            end_index = mid_index - 1                   # we will only search in the left half
        
        else:                                           # the target is greater than mid element
            start_index = mid_element + 1               # we will search only in the right half
    
    return mid_index








for i in range(1, 1000, 1):
    print(array[i])

    x_coordinate.append(i)
    y_coordinate.append(round(time.time() - start, 6))

    print('Time taken: ', round(time.time() - start, 6)) 

    print(array[i])
    print(sqrt(array[i]))



# print(sqrt(27))
# print ("Pass" if  (3 == sqrt(9)) else "Fail")
# print ("Pass" if  (0 == sqrt(0)) else "Fail")
# print ("Pass" if  (4 == sqrt(16)) else "Fail")
# print ("Pass" if  (1 == sqrt(1)) else "Fail")
# print ("Pass" if  (5 == sqrt(27)) else "Fail")



plt.plot(x_coordinate, y_coordinate, marker="o")
plt.xlabel("size")
plt.ylabel("time")
plt.show()



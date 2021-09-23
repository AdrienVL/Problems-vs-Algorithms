def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """

    start_index = 0
    end_index = len(input_list)-1



    while start_index <= end_index:

        mid_index = (start_index + end_index) // 2

        if input_list[mid_index] == number:
            return mid_index

        elif input_list[start_index] == number:
            return start_index

        elif input_list[end_index] == number:
            return end_index


        elif input_list[start_index] > number and number < input_list[mid_index]:
            
            if input_list[mid_index] - input_list[mid_index - 1] == 1 and input_list[mid_index + 1] - input_list[mid_index] == 1:
                end_index = mid_index - 1
                start_index += 1
            else:
                start_index = mid_index + 1
                end_index -= 1

        else: 

            if input_list[mid_index] - input_list[mid_index - 1] != 1 and input_list[mid_index + 1] - input_list[mid_index] == 1:
                end_index = mid_index - 1
                start_index += 1

            else:
                start_index = mid_index + 1
                end_index -= 1


    return -1

def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")

test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])
test_function([[8, 9, 0, 1, 2, 3, 4, 5, 6, 7], 0])
test_function([[4, 5, 6, 7, 0,1,2], 0])

test_function([[10, 24, 26, 16, 0,1,2], 0])




# mid_index = 5
# end_index = 4
# start index = 1




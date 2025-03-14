def sum_using_recursion(test_data):
    new_test_data = test_data[1:]
    return test_data[0]+sum_using_recursion(new_test_data)

test_data = [1,2, [3,4], [5,6]]
print("The sum of the list is ", sum_using_recursion(test_data))


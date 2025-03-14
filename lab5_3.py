def multiply_all_nums(list):
    product = 1
    for i in list:
        product = product*i
    return product

n = int(input("Enter the size of the list"))

list = []
for i in range(0,n):
    element = int(input("Enter the elements of the list"))
    list.append(element)

print("The multiplication of all the numbers in the list is: ", multiply_all_nums(list))
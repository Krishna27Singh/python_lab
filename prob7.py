# new_input = input("Enter the values")

# new_tuple = new_input.split(',')

# print(new_tuple)
# print(len(new_tuple))

# for i in new_tuple:
#     temp_var = i
#     print("\n", temp_var) 

new_list = []
number_of_input = int(input("Enter the number of elements in the list"))

for i in range(number_of_input):
    element = input("Enter the inputs")
    new_list.append(element)

print(new_list)

for i in range(number_of_input):
    new_var = new_list[i]
    print(new_var)

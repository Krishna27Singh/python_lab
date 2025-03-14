def min_of_list(list):
    return min(list)
    

n = int(input("Enter the size of the list"))

list = []
for i in range(0,n):
    element = int(input("Enter the elements of the list"))
    list.append(element)

print(list)

print("The minimum element in the lis is", min_of_list(list))

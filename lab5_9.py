def num_append(list, num):
    bool = False
    for i in list:
        if(i == num):
            bool = True

    if(bool):
        print("the number is already present in the list so cannot be added")
    else:
        list.append(num)

    return list



num = int(input("Enter the number you want to append in the list"))
n = int(input("Enter the size of the list"))

list = []
for i in range(0,n):
    element = int(input("Enter the elements of the list"))
    list.append(element)

print(num_append(list, num))

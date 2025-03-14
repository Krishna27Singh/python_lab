def count_upper_lower(string):
    count_upper = 0
    count_lower = 0
    for i in string:
        if(i>='a' and i<='z'):
            count_lower = count_lower+1
        elif(i>='A' and i<='Z'):
            count_upper = count_upper+1

    print("The number of uppercase letters are ",count_upper, " and the number of lowercase letters are ", count_lower )

    


string = input("Enter the string")

count_upper_lower(string)
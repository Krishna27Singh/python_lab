# strings = list(input("Enter the strings (comma separated): ").split(','))
# new_list = [i for i in strings if i[0]=='a'or i[0]=='e'or i[0]=='i'or i[0]=='o' or i[0]=='u']
# print(strings)
# print(new_list)


data = [("personX", 10), ("personY", 11),("personZ", 31)]
answer = [i for i in data if i[1]>30]
print(answer)
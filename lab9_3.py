strings = list(input("Enter the strings (comma separated): ").split(','))
new_list = [i for i in strings if i[0]=='a'or i[0]=='e'or i[0]=='i'or i[0]=='o' or i[0]=='u']
print(strings)
print(new_list)
check = input("Enter the string")
n = len(check)
count_letters = 0
count_nums = 0
for i in range(0,n):
    if(check[i]>='a' and check[i]<='z' or check[i]>='A' and check[i]<='Z'):
        count_letters = count_letters + 1
    if(check[i]>='1' and check[i]<='9'):
        count_nums = count_nums + 1
print(f"the number of letters in the input string is {count_letters} and the number of numbers in the input string is {count_nums}")
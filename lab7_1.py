inp = input("Enter a string to check if it's palindrome or not")
n = len(inp)
is_palindrome = True
for i in range(0,n):
    if(inp[i]!=inp[n-1-i]):
        is_palindrome = False

if(is_palindrome):
    print("The input string is a palindrome")
else:
    print("The input string is not palindrome")
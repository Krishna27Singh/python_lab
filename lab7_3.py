input = input("Enter the string to reverse")
stack = []
reversed = ""
for i in input:
    stack.append(i)

n = len(stack)
for i in range (0,n):
    reversed = reversed + stack.pop()

print("The reversed string is: ", reversed)


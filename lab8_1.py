inp = tuple(input("Enter the elements in the tuple comma separated: ").split(','))
print(inp)
result = 1
for i in inp:
    result = result*i
print(result)
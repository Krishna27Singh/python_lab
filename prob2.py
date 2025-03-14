a = int(input("Enter the first number"))
b = int(input("Enter the second number"))

print(bin(a))
print(bin(b))

a_str = str(bin(a)[2:])
b_str = str(bin(b)[2:])

print(a_str)
print(b_str)

len_a = len(a_str)
len_b = len(b_str)

print(len_a)
print(len_b)

xor_result = a^b
print(bin(xor_result).count('1'))


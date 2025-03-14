a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

print("The value of numbers before swapping is: ", a, " and ", b)

c = a
a=b
b=c

print("The value of numbers after swapping is: ", a, " and ", b)

#swap integers without using third variable in python

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

print("The value of numbers before swapping is: ", a, " and ", b)

a = a+b
b = a-b
a = a-b

print("The value of numbers after swapping is: ", a, " and ", b)
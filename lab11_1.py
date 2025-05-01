import math_operations
import sys as sys

# sys.path.insert(0, "package1")
# print(sys.path)

num1 = int(input("Enter first number"))
num2 = int(input("Enter second number"))

print(f"The addition of these numbers is: {math_operations.addition(num1, num2)}")
print(f"The substraction of these numbers is: {math_operations.substraction(num1, num2)}")
print(f"The multiplication of these numbers is: {math_operations.multiplication(num1, num2)}")
print(f"The division of these numbers is: {math_operations.division(num1, num2)}")
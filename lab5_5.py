def swap(a, b):
    a = a+b
    b = a-b
    a = a-b
    print("The value of a and b after swapping is ", a, " ", b) 

a = int(input("enter first number"))
b = int(input("enter second number"))

print("The value of a and b before swapping is ", a, " ", b)

swap(a,b)
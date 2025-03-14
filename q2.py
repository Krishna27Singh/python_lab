#sum of two number
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("The sum of numbers is: ", a+b)

#Enter 1 if you are 18, otherwise 0

c = int(input("Enter 0 or 1: "))
if(c!=0 and c!=1):
    print("Enter either 0 or 1")
else:
    if(c): 
        print("you are above 18 and you can drive!")
    else:
        print("You are below 18 and you cannot drive")

sets = {"apple", "banana", "mango"}
print(sets)

dicti = { "1": "papaya",
            "2":  "strawberry",
             "3":  "lichi"}
print(dicti["1"])
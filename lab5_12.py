def is_factor(f, n):
    if(n%f == 0):
        print("f is a factor of n")
    else:
        print("f is not a factor of n")

f = int(input("Enter the value of f "))
n = int(input("Enter the value of n "))

is_factor(f,n) 
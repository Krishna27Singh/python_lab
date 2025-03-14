n = int(input("enter the number"))

sum = 0

while(1):
    mod = n%10
    n = n//10
    if(n != 0):
        sum = sum+mod
    else:
        break

print(sum)
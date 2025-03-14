n = int(input("Enter the value of n"))

t1 = n-1
sum =1


for i in range(2,n):
    condition = 0
    for j in range(2,i):
        if(i%j==0):
            condition = 1
            break
        else:
            j=j+1
    
    if(condition==0):
        sum = sum+i


print(sum)
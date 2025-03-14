def n_prime(n, list, count):
    while(True):
        for i in range(2,count):
            if(count%i == 0):
                count = count +1 
                continue
        list.append(count)
        count = count+1
        if(len(list) == n):
            break

    return list


list = []
list.append(1)
n = int(input("Enter the value of n"))

count = 2

print(n_prime(n, list, count))
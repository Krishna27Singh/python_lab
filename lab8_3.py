def func(*v_arg):
    print(v_arg[0])
    sum=0
    prod=1
    for i in v_arg[0]:
        sum=sum+int(i)
    for i in v_arg[0]:
        prod = prod*int(i)
    tup = (sum,prod)
    return tup

tup = tuple(input("Enter the value in tuples comma separated:").split(','))
result = func(tup)
print(result) 
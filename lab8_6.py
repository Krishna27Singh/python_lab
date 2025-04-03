tup = ((1,2,6),(3,4,11,5),(23,53),(22,12,1,3,4),(5,6))
new = list(tup)
print(new)
n = len(tup)
for j in range(0,n):
    for i in range(0,n-1):
        if(new[i][1]>new[i+1][1]):
            new[i],new[i+1]=new[i+1],new[i]
final = tuple(new)
print(final)
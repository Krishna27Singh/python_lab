list = [2,5,3,1,6,8,7,4,9]

#BUBBLE SORT
i = 0
while(i<len(list)):
    j = 0
    while(j<len(list)-1):
        if(list[j]>list[j+1]):
            list[j], list[j+1] = list[j+1], list[j]
        j = j+1
    i = i+1

print(list)

#BINARY SEARCH
a = int(input("Enter the number to search"))

start = 0
end = len(list)-1
mid = int(start + (end-start)/2)
isFind = False

while(start<=end):
    if(list[mid] == a):
        print("The element to search is at the index ", mid)
        isFind = True
        break
    elif(list[mid] > a):
        end = mid-1
    elif(list[mid] < a):
        start = mid+1
    
    mid = int(start + (end-start)/2)

if(isFind == False):
    print("Element not found!")
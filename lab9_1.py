dicti = {
    "instagram": 9,
    "facebook": 8,
    "whatsapp": 3,
    "twitter": 5,
}

key1 = input("Enter the key you want to add to the dictionary")
value1 = int(input("Enter the value corresponding to the key"))
dicti[key1]= value1
print(dicti)

key2=input("Enter the key whose value you want to change")
value2=int(input("Enter the value"))
dicti[key2]=value2

platform=input("Enter the platform you want to delete from the dictionary")
dicti.pop(platform)

print(dicti)

print(dicti.values())
print(dicti.keys())

for i in dicti:
    print(i)

max_value = -1
for i in dicti:
    max_value = max(max_value,dicti[i])

for i in dicti:
    if(dicti[i]==max_value):
        answer = i

print("The key with hightest value is ", answer)
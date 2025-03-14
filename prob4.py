list1 = list(input("Enter the first list"))

newlist = []

for i in list1:
    if i not in newlist:
        newlist.append(i)

# print(list1.remove('2'))
# for i in list1:
#     list2 = list(list1.remove(i))
#     if i not in list2:
#         continue
#     else:
#         list1.remove(i)

print(newlist)
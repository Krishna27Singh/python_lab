#python lists are container to store any type of data type

friends = ["Apple", "Orange", 5, 345.06, False, "Aakash", "Rohan"]

print(friends[0])
friends[0] = "Grapes" # Unlike Strings lists are mutable

print(friends[0])
print(friends[1:4])

######### METHODS IN LIST #########

lovers = ["krishna", "shalini", 5, 7.5, True, "krisha"]
print(lovers)

lovers.append("krini")
print(lovers)
#append function lit ke end m jo input dete vo include krdeta hai list m
#list ke andr agr hum koi function use krte hai to list hi change ho jati hai 
num = [2,5,7,23,1,5]
num.sort()
#ascending order m arrange krdega
print(num)
num.sort(reverse = True)
print(num)
lovers.reverse()
print(lovers)
lovers.insert(0,"krishnaaaaa")
print(lovers)
# SYNTAX--- list_name.inset(index, element_you_want_to_insert)
#lovers.pop(0)
print(lovers)
print(lovers.pop(0))
#lovers.pop(0) --- list m 0th index ki value delete krdega aur vahi value return krega 
lovers.remove("krini") #idhr index nhi element mention krna hai
print(lovers)
lovers.extend(["krini", "krishnaaaaa"])
print(lovers)
print(lovers.index("krishna"))
print(lovers)
print(lovers.count("krishna"))
print(lovers)
lovers.clear()
print(lovers)
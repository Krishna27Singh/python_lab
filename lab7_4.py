string1 = input("Enter the first string")
string2 = input("Enter the second string")
n1 = len(string1)
n2 = len(string2)
final_string = ""
count = 0
for i in string2:
    if(count==2):
        break
    final_string = final_string+i
    count = count+1
count = 0
for i in string1:
    if(count>1):
        final_string = final_string+i
    count = count+1
count = 0
final_string = final_string+" "
for i in string1:
    if(count==2):
        break
    final_string = final_string+i
    count = count+1
count = 0
for i in string2:
    if(count>1):
        final_string = final_string+i
    count = count+1
print(final_string)
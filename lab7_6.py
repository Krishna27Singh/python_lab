num = input("Enter the number: ")
stack = []
answer = ""
for i in num:
    stack.append(i)
count = 0
for i in stack:
    count = count+1
    if(count%3==0):
        answer = answer + ","
    answer = answer + i
print(answer)
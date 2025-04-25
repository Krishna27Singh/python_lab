# first code
# for i in range(1, 6):
#     print(*range(1, i+1))

# sec
# for i in range(1, 6):
#     print(" "*(5-i) + "* " * i)

# thi
# for i in range(5, 0, -1):
#     print("* " * i)

# four
# n = 5
# for i in range(1, n + 1):
#     print(" " * (n - i), end="")
#     for j in range(1, i + 1):
#         print(j, end=" ")
#     print()
# print("1 2 3 4 5 6 7 8 9")                   

# five
# for i in range(9, 0, -2):
#     print(" " * ((9 - i) // 2), *range(1, i + 1))
# for i in range(3, 10, 2):
#     print(" " * ((9 - i) // 2), *range(1, i + 1))




# x=print
# x("hello")
# a,*b,c,d=(1,2,3,4,5,6,7)
# print(a)
# print(b)
# print(c)

# lis=[2,3,4,6,7]
# print(lis.pop())

# tup=([2,3,4,6,7],[3,5,3])
# print(tup[0])
# print(id(tup[0]))
# print(id(tup[0][0]))
# tup[0][0]=10
# print(tup[0])
# print(id(tup[0]))
# print(id(tup[0][0]))


# a={}
# b={None,None}
# print(type(a),type(b))
# a="1,2,3,4,5,6,7,8,9".split(",",20)
# print(a)

# list1=[[1,2,3],3,[8,3]]
# new_list=[2,3]
# # new_list.append(list1)
# # print(new_list)
# new_list.extend(list1)
# print(new_list)

d={"s":2,'4':8,"9":5}
print(d.pop())
print(d)
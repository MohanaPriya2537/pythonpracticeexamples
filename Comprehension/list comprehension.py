# To print even no
#
# l=[]
# for i in range(10):
#     if(i%2==0):
#         l.append(i)
# print(l)
#              or
# a=[i for i in range(10) if (i%2==0)]

# a='developer'
# b=list(a)
# print(b)

# To display in list format
# a='developer'
# # l=[]
# # for i in a:
# #     l.append(i)
# # print(l)
# #       or
# b=[i for i in a]
# print(b)

# To write a program for cube of a list
# a=[2,8,5,3]
# l=[]
# for i in a:
#     l.append(i**3)
# print(l)
# # or
#
# b=[i**3 for i in a]
# print(b)

# # Square of list
# l=[1,2,3,4]
# a=list(map(lambda i:i*i,l))
# print(a)

# To display no divisible from 2 and 5
# l=[]
# for i in range(20):
#     if(i%2==0 and i%5==0):
#         l.append(i)
# print(l)
# or
# a=[i for i in range(20) if(i%2==0 and i%5==0)]
# print(a)

# To multiply the list
a=[1,2,3]
b=[4,5,6]
c=[]
for i in a:
    for j in b:
        prod=i*j
        c.append(prod)
print(c)
# or
# a=[1,2,3]
# b=[4,5,6]
# c=[i*j for i in a for j in b]
# print(c)




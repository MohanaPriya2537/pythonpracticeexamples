# #Creating a set
# setx=set()
# print(setx)
# #
# #a={10,'pen','hello',25}
# # #Accesing a set
# # for x in a:
# #     print(x)
# #
# # #Adding an element
# # a.add('June')
# # print(a)
# #
# # #Removing an element
# # # a.remove('hello')
# # # print(a)
# #
# # #Updating an element
# # a.update(['December','March'])
# # print(a)
# #
# # #Length of set
# # print(len(a))
#
# #Clear a set
# # a.clear()
# # print(a)
#
# #Delete a set
# # del a
# # print(a)
#
# # a={1,2,3,4,5}
# # b={2,5,6,8}
# # d={2,5}
#
# #Union of sets
# # c=a|b
# # print(c)
#
# #Intersection of sets
# # c=a&b
# # print(c)
#
# #Difference of sets
# # c=a-b
# # print(c)
#
# #copy()
# # c=a.copy()
# # print(c)
#
# #Discard()
# # a.discard(10)
# # print(a)
#
# #isdisjoint()
# # c=a.isdisjoint(b)
# # print(c)
#
# #issubset()
# a={1,2,3,4,5}
#
# d={1,2}
# # c=a.issubset(b)
# # print(c)
# x=a.issubset(d)
# print(x)
#
# #Symmetric Difference
# # a={1,2,3,4,5}
# # b={2,8,10,12}
# # c=a.symmetric_difference(b)
# # print(c)
# #
# # #pop
# # a.pop()
# # print(a)

a={1,2,3,4,5}
b={1,2}
c=a.issubset(b)
print(c)
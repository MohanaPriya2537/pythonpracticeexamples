# from functools import reduce
# l=[1,2,3,4,5]
# # x=lambda a,b:a+b,l
# # print(x)
# add=reduce((lambda a,b:a+b),l)
# print('Addition:',add)
#
# sub=reduce((lambda a,b:a-b),l)
# print('Sub:',sub)
#
# pro=reduce((lambda a,b:a*b),l)
# print('Multiplication:',pro)

# from functools import reduce
# # def prod(a,b):
# #     return a*b
# # x=reduce(prod,range(1,5))
# # print(x)

from functools import reduce
def sum(a,b):
    return a+b
x=reduce(sum,range(1,5))
print(x)
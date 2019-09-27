# To convert a list to set
# a=set()
# for i in range(20):
#     a.add(i)
# print(a)
# or
# a={i for i in range(20)}
# print(a)

# To multiply the set
# a={1,2,3}
# b={4,5,6}
# c=set()
# for i in a:
#     for j in b:
#         prod=i*j
#         c.add(prod)
# print(c)
# or
a={1,2,3}
b={4,5,6}
c={i*j for i in a for j in b}
print(c)



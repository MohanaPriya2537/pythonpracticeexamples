# To print the cube with displaying both the values and keys
# a={1,2,3,4}
# b={}
# for i in a:
#     b[i]=i**3
# print(b)
# or
# a={1,2,3}
# b={i:i**3 for i in a}
# print(b)

# a=[1,2,3]
# b=[4,5,6]
# c={}
# for k,v in zip(a,b):  ##zip is a method()
#     c[k]=v
# print(c)
# or
a=[1,2,3]
b=[4,5,6]
c={k:v for k,v in zip(a,b)}
print(c)
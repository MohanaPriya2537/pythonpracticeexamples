
import re
n=input("Enter the pattern:")
b='123456789 123 234 345'
m=re.findall(n,b)
print(m)
# if m.__contains__(n):
#     print(m)
# else:
#     print("NO")
# if m!=None:
#     print12
# else:
#     print('Not matched')
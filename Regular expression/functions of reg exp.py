# #Search():Checks the pattern in all the ways 1st, middle and last
# import re
# n=input("Enter the pattern:")
# matcher=re.search(n,'Life is beautiful')
# if (matcher!=None):
#     print('Match found')
# else:
#     print('Match not found')

# #match():Checks only from the start index
# import re
# n=input("Enter the pattern:")
# matcher=re.match(n,'Life is beautiful')
# if (matcher!=None):
#     print('Match found')
# else:
#     print('Match not found')

#fullmatch():Checks if the complete pattern matches with the targetted pattern
# import re
# n=input("Enter the pattern:")
# matcher=re.fullmatch(n,'Life is beautiful')
# if (matcher!=None):
#     print('Match found')
# else:
#     print('Match not found')

#finditer()
# import re
# n=input("Enter the pattern:")
# matcher=re.finditer(n,'abcefg')
# if (matcher!=None):
#     for m in matcher:
#         print(m.start(),m.group(),m.end())
#     print('Match found')
# else:
#     print('Match not found')

# findall:Returns all the values in the list
import re
n=input("Enter the pattern:")
b='123456789'
m=re.findall(n,b)
if m!=None:
    print('Matched')
else:
    print('Not matched')

# Sub()-->It is replacement string
# import re
# m=re.sub('\d','$','ac25efg07')
# print(m)

# # Subn-->>No of replacement of the string
# import re
# t=re.subn('\d','$','ac25efg07')
# print(type(t))
# print("Result string:",t[0])
# print("No of replacement:",t[1])

# Split()-->Returns the values in the list. Explicitly should enter the way it should be splited.
# import re
# l=re.split('-','10-20-30-40')
# print(l)

# import re
# m=re.split('-','www-gmail-com')
# for x in m:
#     print(x)
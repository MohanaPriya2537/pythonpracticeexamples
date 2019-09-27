# #Compile method
# import re
# x=re.compile('python')
# print(type(x))
#
# # Finditer:Checks whether the pattern is repeating and gives the index value
# import re
# pattern=re.compile('python')
# matcher=pattern.finditer('learning python')
# for i in matcher:
#     print(i.start())
#
# import re
# pattern=re.compile('n')
# matcher=pattern.finditer('learning python')
# for i in matcher:
#     print(i.start())
#     print(i.end())


import re
count=0
x=re.finditer('ab','abaabbab')
for i in x:
    print(i.start())
    print(i.end())     #end will take end+1
    print(i.group())
    count=count+1
print('No of times it is iterated is :',count)
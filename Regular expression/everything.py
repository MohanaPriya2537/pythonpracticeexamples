#Findall-Returns the values in list0(Cant use start,end and group(repeatation not possible))

# import re
# x = "python3,is easy to learn"
# r = re.findall("^\w+",x)
# print(r)

# import re
# a = re.findall("t", "We need to inform him about the timings!")
# for i in a:
#     print(i)

# import re
# str = "python3,is easy to learn and easy to do programming"
# x = re.findall("easy", str)
# print(x)

#finditer()->Can use start,end and group(repeatation is possible)

# import re
# Str = "we need to inform him with the latest information"
# for i in re.finditer("inform.", Str):
#     print(i.span())

# search()

# import re
# str = "python3 is easy to learn"
# x = re.search("\s", str)
# print("The first white-space character is located in position:", x.start())

# import re
# if re.search("python", "we need to inform abt the timings"):
#     print("There is information")
# else:
#     print("There is no information")

import re
x = "software develeoper in techpark"
print(re.search('techpark', x))  #returns objects
print(re.search('part', x))    #if doesnt exist in the pattern it will return NONE

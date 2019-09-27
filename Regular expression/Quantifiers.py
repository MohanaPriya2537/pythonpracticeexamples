# #a->excatly one a
# import re
# matcher=re.finditer('a','abaabaaab')
# for m in matcher:
#     print(m.start(),m.group())

# print('**********')
#
# #a+ -> atleast one a
# import re
# matcher=re.finditer('a+','abaabaaab')
# for m in matcher:
#     print(m.start(),m.group())
#
# print('*********')
#
# # a*->any no of a including zero
import re
matcher = re.finditer('a*', 'abaabaaab')
for m in matcher:
    print(m.start(), m.group())
#
# print('**********')
#
# # a? -> either 1 or n no of a's
# import re
# matcher = re.finditer('a?', 'abaabaaab')
# for m in matcher:
#     print(m.start(), m.group())
#
# print('**********')
#
# # a{n}->n no of times a is printed
# import re
# matcher = re.finditer('a{n}', 'abaabaaab')
# for m in matcher:
#     print(m.start(), m.group())
#
# print('**********')
#
# # a{m,n}-> returns the max n min no of times a is printed
# import re
# matcher = re.finditer('a{m,n}', 'abaabaaab')
# for m in matcher:
#     print(m.start(), m.group())
#
# print('**********')
#
# # [^a]->returns except a if it is inside the list
# import re
# matcher = re.finditer('[^a]', 'abaabaaab')
# for m in matcher:
#     print(m.start(), m.group())
#
# print('**********')
#
# # ^a -> checks whether a is in the start index
# import re
# matcher = re.finditer('^a', 'abaabaaab')
# for m in matcher:
#     print(m.start(), m.group())
#
# print('**********')
#
# # a$->checks n returns if a is in the last index
# import re
# matcher = re.finditer('a', 'abaabaaab')
# for m in matcher:
#     print(m.start(), m.group())
#
# print('**********')
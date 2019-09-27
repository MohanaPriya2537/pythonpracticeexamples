#Calculate the no of digits and letter in a string

str="023asd"
d=0
l=0
for x in str:
    if x.isalpha():
        l=l+1
    elif x.isdigit():
        d=d+1
    else:
        pass
print("Letter:", l)
print("Digit:", d)

# s = "123asd"
# d=l=0
# for c in s:
#     if c.isdigit():
#         d=d+1
#     elif c.isalpha():
#         l=l+1
#     else:
#         pass
# print("Letters", l)
# print("Digits", d)
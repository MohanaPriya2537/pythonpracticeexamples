str=input("Enter the string value")
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

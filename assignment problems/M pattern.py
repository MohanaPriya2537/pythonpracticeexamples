# Program to print the alphabet M

str=""
for r in range(0,7):
    for c in range(0,7):
        if(c==1 or c==5 or (r==2 and (c==2 or r==4)) or (r==3 and c==3)):
            str=str+"*"
        else:
            str=str+" "
    str = str + "\n"
print(str)

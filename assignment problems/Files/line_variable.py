# To read an entire text file using function
f=open("fname.txt",'w')
f.write('hi hello')
f.close()
def fread(fname):
    f=open('fname.txt','r')
    a=f.readlines()
    print(a)
fread('var.txt')

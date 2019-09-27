# To copy from one file to another
# f=open('abc.txt','w')
# a=['hi\n','hello\n','GM']
# f.writelines(a)
# f.close()
# f=open('abc.txt','r')
# a=f.read()
# # a=f.readlines()
# print(a)
# f=open('xyz.txt','w')
# b=f.writelines(a)

# Exclusive mode is creating a new file with the same content i.e present in the existing file
f=open('test.txt','x')
f.write("Hi hello")
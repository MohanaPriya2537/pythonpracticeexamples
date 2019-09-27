# f=open("abc.txt",'w')
# # f=open("../file/a.txt",'w') doubt
# # f=open("../a.txt",'w')
# f.write("Python class")
# f.write("Welcome")

# f=open("abc.txt")
# print('read',f.read())


# to print multiple lines
# f=open("abc.txt",'w')
# list=['hi\n','hello']
# f.writelines(list)

# to use write multiple lines in the same file
# f=open("abc.txt",'w')
# f.write("Hello\n")
# f.close()
# f=open("abc.txt",'a')
# f.writelines("GM")

# to use r+,w+
# f=open("abc.txt",'w+')
# f.write("hello")
# print(f.read())  (doubt)

# f=open("abc.txt")
# print('name',f.name)
# print('mode',f.mode)
# print('writable',f.writable())
# print("readable",f.readable())
# print("closed",f.closed)

# f=open('abc.txt','w')
# a=['hi\n','hello\n','GM']
# f.writelines(a)
# f.close()
# f=open('abc.txt','r')
# a=f.read()
# print(a)
# f=open('abc.txt','r')
# b=f.readline()
# print(b)
# c=f.readline()
# print(c)
# f=open('abc.txt','r')
# c=f.readlines()
# print(c)

# f=open('abc.txt','w')
# a=['hi\n','hello\n','GM']
# f.writelines(a)
# f.close()
# f=open('abc.txt','r')
# b=f.readlines()
# # print(b)
# for i in b:
#     print(i)
#     # print(i,end='')



# To use all the modes
# with open('abc.txt','w+') as f:
#     f.write("Hi Hello GM")
#     f.read()
#     f.seek(0)
# f.close()
# f=open('abc.txt','r+')
# print(f.read())
# # print(f.seek(2))
# f.close()
# a=open('abc.txt','a+')
# b=a.write('\nWelcome')

# To find whether the given file exist or no
# import os
# fname=input("enter file name:")
# if os.path.isfile(fname):
#     f=open(fname,'r')
#     print(f.read())
# else:
#     print("file not exit")








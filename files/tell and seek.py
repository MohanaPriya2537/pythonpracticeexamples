# tell() is like indexing
# f=open('abc.txt','w')
# f.write("Hihello")
# f=open('abc.txt','r')
# print(f.read())
# print(f.tell())
# print(f.read(2))
# print(f.tell())
# print(f.read(3))
# print(f.tell())
# print(f.read(0))
# print(f.seek(0))

# seek() is like forwarding
# f=open('abc.txt','w')
# f.write("Hi hello")
# f=open('abc.txt','r')
# print(f.read())
# print(f.seek(2))
# print(f.read())

# Exclusive mode
# f=open('test.txt','x')
# f.write("Hi hello")

f=open('asd.txt','w+')
# f.write('Hi Hello')
print(f.read())
print(f.seek(0))

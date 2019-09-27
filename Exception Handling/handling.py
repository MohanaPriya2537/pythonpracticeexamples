# try:
#     a=10
#     b='0'
#     print(a+b)
#     # print(a/b)
# except(TypeError):
#     print('TYPE ERROR')
# except(ZeroDivisionError):
#     print('zero error')

# Type error
# try:
#     a=10
#     b='0'
#     print(a+b)
# except:
#     print('TYPE ERROR')

# Syntax error
# try:
#     a=10
#     print(a+b)
# except:
#     print('Syntax error')

# # Name error
# try:
#     print(a)
# except:
#     print('Name error')

# a=10
# print(a+b)    error:name error

# Zero division error and arithematic error
# try:
#     a=10
#     b=0
#     print(a/b)
# except:
#     print('Zero division error')

# a=10
# b=0
# print(a/b)  #ZeroDivisionError: division by zero

#File Not Found Error:
# f=open('abc.txt')
# print(f.read())         #FileNotFoundError:

# try:
#     f=open('abc.txt')
#     print(f.read())
# except:
#     print('File Not Found Error')

#Use of else: If try condition is correct it will execute the else part and if try condition is not satisfied except will be executed
# try:
#     a=10
#     b=20
#     print(a*b)
# except:
#     print('Exception occurred')
# else:
#     print(('No exception occurred'))
# finally:
#     print('thank you')

#Value error
# int('str')    #ValueError:

# try:
#     int('str')
# except:
#     print('Value error')

# Index Error
# l=[1,2,3,5]
# print(l[5])

# try:
#     l=[1,2,3,5]
#     print(l[5])
# except:
#     print('Index error')
#     import sys
#     print(sys.exc_info())
# finally:
#     print('Close the file')





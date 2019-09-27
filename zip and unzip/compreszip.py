# To zip all the files
# from zipfile import *
# f=ZipFile('hi.zip','w',ZIP_DEFLATED)
# f.write('../abc.txt')
# f.write('../files/test.txt')
# f.close()

# To check the no of folders in a zipped file
# from zipfile import *
# f=ZipFile('hi.zip','r',ZIP_STORED)
# names=f.namelist()
# for i in names:
#     print(i)

# To read the contents from the zipped file
# from zipfile import *
# f=ZipFile('hi.zip','r',ZIP_STORED)
# names=f.namelist()
# for i in names:
#     print(i)
#     print('The contents from hi.zip is:')
#     a=open(i)
#     print(a.read())
#     print('*'*10)       #to differentiate from one file content to another

# To extract the file
# from zipfile import *
# with ZipFile('hi.zip','r') as f:
#     f.extractall('temp')

import os
# cwd=os.getcwd()             #to get the current directory
# print(cwd)
# os.mkdir('Fresh folder')       #to create a directory
# os.makedirs('GM')      #to create multiple directory
# print("Successfully created")
# os.rename('Old folder','N files')
# print('Renamed successfully')
# os.rmdir('New folder')         #to remove a directory
# os.removedirs('hi hello')
# print('Removed')
# a=os.listdir('.')
# for i in a:
#     print(len(i))

# import os
# os.removedirs('GM')  #'N files','Fresh folder','New files','GM')
# print('removed')

# To find the length of the folder
# a=os.listdir('.')
# for i in a:
#     print(i)
# print(len(a))

# hi=os.listdir('..')
# for i in hi:
#     print(i)

# import os
# # cwd=os.getcwd()             #to get the current directory
# # print(cwd)
# os.remove('hi.zip')


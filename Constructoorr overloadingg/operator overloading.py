# class Book:
#     def __init__(self,x):
#         self.pages=x
# b=Book(100)
# print(b)

# Example for operator overloading
# class Book:
#     def __init__(self,x):
#         self.pages=x
#
#     def __add__(self, other):
#         return self.pages+other.pages
#
# b1=Book(100)
# b2=Book(200)
# print(b1+b2)


# Example using string operator overloading
# class Book:
#     def __init__(self,x):
#         self.pages=x
#
#     def __str__(self):
#         return ('No of pages are ' + str(self.pages))
#
#     def __add__(self, other):
#         total=self.pages+other.pages
#         b=Book(total)
#         return b
#
# b1=Book(100)
# b2=Book(200)
# b3=Book(300)
# b4=Book(400)
# print(b1+b2+b3+b4)

# class Student:
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks
#
#     def __lt__(self, other):
#         return self.marks<other.marks
#
# s1=Student('Priya',80)
# s2=Student('Arun',90)
# print(s1<s2)
#
# class Student:
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks
#
#     def __gt__(self, other):
#         return self.marks>other.marks
#
# s1=Student('Priya',80)
# s2=Student('Arun',90)
# print(s1>s2)



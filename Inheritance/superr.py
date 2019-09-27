# To call

# class Parent:
#     def property(self):
#         print('cash+land+gold')
#     def marriage(self):
#         print("Priya")
# class Child(Parent):
#     def marriage(self):
#         super().marriage()
#         print("Arun")
# c=Child()
# c.property()
# c.marriage()

# class College:
#     def info(self,name,age):
#         self.name=name
#         self.age=age
# class Student(College):
#     def details(self):
#         super().info()
#         print('My name is:', self.name)
#         print('My age is:', self.age)
# s=Student('Priya',25)
# s.details()


# class College:
#     def name(self):
#         print("My name is Priya")
#     def age(self):
#         print("My age is 25")
# class Student:
#     def rollno(self):
#         print("My roll number is 32")
#     def marks(self):
#         print("My first semesterpercentage is 80%")
# class Info(College,Student):
#     def marks(self):
#         super().marks()
#         print("My second semester percentage is 82%")
# a=Info()
# a.name()
# a.age()
# a.rollno()
# a.marks()




class Animal(object):
    def __init__(self, name, colour):
        self.name = name
        self.colour = colour

class Baby(Animal):
    def __init__(self, babyname):
        super().__init__()
        self.babyname = babyname

a=Baby(Dog,Black,Puppy)
a.babyname 00
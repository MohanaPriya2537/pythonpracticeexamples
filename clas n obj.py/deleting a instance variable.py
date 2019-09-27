# Deleting within class using self
class Student:
    def __init__(self):
        self.a=10
        self.b=20
        self.c=30
        self.d=40
    def delete(self):
        del self.a
        del self.b
s=Student
s.delete()
print(s.__dict__)

# Explicitly deleting outside using variable
# class Student:
#     def __init__(self):
#         self.a=10
#         self.b=20
# s=Student()
# del s.a
# print(s.__dict__)
# class Student:
#     '''This is my first class'''
# print(Student.__doc__)
# help(Student)
#
# class test:
#     x="Hello word"
# print(test)


class A:
    def a(self):
        print(1)


class B(A):
    def a(self):
        print(2)


class C(B):
    def c(self):
        print(3)


c = C()
c.a()
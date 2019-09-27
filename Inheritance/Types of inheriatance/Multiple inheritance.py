# class Parent1:
#     def m1(self):
#         print("Parent 1 method")
# class Parent2:
#     def m2(self):
#         print("Parent 2 method")
# class Child(Parent1,Parent2):
#     def m3(self):
#         print("Child method")
# c=Child()
# c.m1()
# c.m2()


class A:
    def sum(self,a,b):
        print(a+b)
class B:
    def sub(self,a,b):
        print(a-b)
class C:
    def prod(self,a,b):
        print(a*b)
class D(A,B,C):
    def divide(self,a,b):
        print(a/b)
d=D()
d.sum(10,20)
d.sub(20,30)
d.prod(2,3)
d.divide(20,5)
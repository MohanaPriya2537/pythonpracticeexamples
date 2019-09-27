class Parent:
    def m1(self):
        print("Parent method")
class Child(Parent):
    def m2(self):
        print("Child method")
p=Parent()
p.m1()
c=Child()
c.m1()
c.m2()


class Animal:
    def eat(self):
        print("Animal Speaking")
class Dog(Animal):
    def bark(self):
        print("Dog barks")



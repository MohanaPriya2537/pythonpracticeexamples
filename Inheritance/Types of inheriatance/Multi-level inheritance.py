class Parent:
    def m1(self):
        print("Parent method")
class Child(Parent):
    def m2(self):
        print("Child method")
class Subchild(Child):
    def m3(self):
        print("Sub-child method")
sc=Subchild()
sc.m2()
sc.m3()
sc.m1()

class Animal:
    def speak(self):
        print("Animal Speaking")
# The child class Dog inherits the class base Animal
class Dog(Animal):
    def bark(self):
        print("Dog Barking")
# The child class Dogchild inherits another child class Dog
class Dogchild(Dog):
    def eat(self):
        print("Eating bread")
d=Dogchild()
d.speak()
d.bark()
d.eat()

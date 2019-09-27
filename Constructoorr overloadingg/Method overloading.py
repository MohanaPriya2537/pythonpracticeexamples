class Student:
    def __init__(self,name,age):
        print('Constructor execution')
        self.name=name
        self.age=age

    def display(self):
        print("Method overloading")
        print("Hello I am ",self.name)
        print("My age is ",self.age)

s=Student('Priya',20)
s.display()
s.display()
s.display()
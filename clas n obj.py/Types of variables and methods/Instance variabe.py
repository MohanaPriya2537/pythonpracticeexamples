class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def talk(self):
        print('My name is:',self.name)
        print('My age is:',self.age)
s1=Student('Priya',25)
s1.talk()
print('\n')
s2=Student('Arun',27)
s2.talk()
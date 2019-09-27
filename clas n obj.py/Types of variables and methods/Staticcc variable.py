#Static variable/Local varible
class Student:
    def __init__(self):
        self.name='Priya'
        self.age=25
    def talk(self):
        print('My name is:',self.name)
        print('My age is:',self.age)
s=Student()
s.talk()

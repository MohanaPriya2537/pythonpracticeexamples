class Test:
    def __init__(self):
        self.a=10
        self.b=20
        self.c=30
    def m1(self):
        self.d=40
    def m2(self):
        self.e=50
t=Test()
t.m1()                  #within class using self
print(t.__dict__)
# t1=Test()
# t1.m2()
# print(t1.__dict__)
t2=Test()
t2.m2()
t2.f=60                #outside class using object variable
print(t2.__dict__)
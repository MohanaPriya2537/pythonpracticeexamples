class Parent:
    def property(self):
        print('cash+land+gold')
    def marriage(self):
        print("Priya")
class Child(Parent):
    def marriage(self):
        print("Arun")
c=Child()
c.property()
c.marriage()
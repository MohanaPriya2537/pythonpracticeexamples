# class test:
#     def __init__(self):
#         print('Software Developer')
# t=test()

# Example for self
class test:
    def __init__(self):
        print('Software Developer')
        print(id(self))
t=test()
print(id(t))

# class test:
#     def __init__(self):
#         print(10+20)
# t=test()
# t1=test()
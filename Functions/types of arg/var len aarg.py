# def year(*months):
#     for i in months:
#         print(i)
# year('jan','feb','june','dec')
#
# def test(*arg):
#     sum=0
#     for i in arg:
#         sum=sum+i
#     print(sum)
# test(10,20)

# def display(**arg):
#     print("Emp details")
#     for i,j in arg.items():
#         print(i,j)
# display(eid=100,ename='priya',esalary=20000)

# def display(**arg):
#     print(type(arg))
#     print("Emp details")
#     for i,j in arg.items():
#         print(i,j)
# display(eid=100,ename='priya',esalary=20000)
#
# stud_name=input("Enter the student name")
# stud_age=input("Enter the student age")
# stud_addr=input("Enter the student address")
# def display(**arg):
#     print("Emp details")
#     print("Student name:",stud_name)
#     print("Student age:",stud_age)
#     print("Student address:",stud_addr)
# display(stud_name,stud_age,stud_addr)

def test(**kwargs):
    for k,v in kwargs.items():
        print(k,':',v)
test(sname='priya',sage=20,saddress='bangalore')

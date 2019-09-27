# Position arg
# def emp(empid,esalary):
#  emp(101,25000)
#
# #Keyword arg
# def emp(empid,esalary):
#     emp(empid=101,esalary=30000)
#     emp(101,esalary=20000)

#Default arg
def emp(empid,empsalary=25000):
    print("Employee Details")
emp(empsalary=30000)
#output:TypeError: emp() missing 1 required positional argument: 'empid'
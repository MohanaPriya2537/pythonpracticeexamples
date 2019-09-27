# if stmt
# a=10
# if (a<=20):
#     print(a)


# if else stmt
# a=10
# b=20
# if(a>b):
#     print(a)
# else:
#     print(b)

#if else stmt
# a=10
# if(a%2==0):
#     print("Even")
# else:
#     print("Odd")

# else if stmt
# a=5
# if(a%2!=0):
#     print("Odd")
# else:
#     print("Even")

# elif stmt
# a=10
# b=20
# if(a>b):
#     print("Greater")
# elif(a==b):
#     print("Equal")
# else:
#     print("Lesser")

# nested if stmt
# today="Holiday"
# bank_bal=25000
# if(today=="Holiday"):
#     if(bank_bal==25000):
#         print("Go to trip")
#     else:
#         print("No trip")
# else:
#     print("Working day")

#FOR LOOP
# x=[1,2,3,4]
# for i in x:
#     print("x")

# n=2
# for i in range(1,11):
#     print(n*i)

#Sum of imtegers
# sum=0
# for i in range(1,11):
#     print(sum+i)

# sum=0
# for i in range(1,11):
#     sum+=i
#     print(sum)

#while loop
# i=1
# while(i<=5):
#     print(i)
#     i=i+1

# #Even no
# n=2
# while(n%2==0):
#
#         print("n")

#Break stmt
# for i in range(1,11):
#     if(i==6):
#         break
#     print(i)

#Continue stmt
# for i in range(1,11):
#     if(i==6):
#         continue
#     print(i)


nums = {1, 2, 3, 4, 5, 6}
nums = {0, 1, 2, 3} & nums
nums = filter(lambda x: x > 1, nums)
print(len(list(nums)))










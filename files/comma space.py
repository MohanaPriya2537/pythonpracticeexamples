# # To write the CSV file
# import csv
# with open('Student.csv','w',newline='') as f:
#     w=csv.writer(f)
#     w.writerow(['Name','ID','Marks'])
#     while True:
#         name=input("Enter the student name:")
#         id=int(input("Enter the student id:"))
#         marks=float(input("Enter the student marks:"))
#         w.writerow([name,id,marks])
#         x=input("Do you want to enter one more records (Yes|No)")
#         if x.lower()=='no':
#           break

# # # To read the CSV file
# import csv
# with open('Student.csv', 'r',newline='') as f:
#     r=csv.reader(f)
#     data=list(r)
#     print(data)
#     # # or
#     # for i in r:
#     #     print(i)
# #     or
#     for row in data:
#         print(row[0],row[1],row[2],sep='\t')
# f.close()


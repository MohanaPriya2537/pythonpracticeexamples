# To use r+ for csv file
import csv
f=open('Student.csv','r+')
r=csv.reader(f)
w=csv.writer(f)
data=list(r)
for row in data:
    if row[3]=='priya':
        w.writerow([row[0],10,row[1]])
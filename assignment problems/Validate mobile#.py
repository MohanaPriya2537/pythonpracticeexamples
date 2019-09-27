import re
n=input('Enter the mobile number:')
m=re.fullmatch('[6-9]\d{9}',n)
if m!=None:
    print('Valid no')
else:
    print('Invalid no')
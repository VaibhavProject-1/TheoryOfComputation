import re

txt=input('Enter string:')
x=re.search("[i]",txt)
if x:
    print("Matched")
else:
    print("Not matched")

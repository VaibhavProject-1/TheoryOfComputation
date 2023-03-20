str1=input("Enter the string:")
str2=input("Enter second string:")
one="1"
zero="0"
count1=0
count2=0
for one in str1:
    count1+=1
for zero in str2:
    count2+=1
if count1==count2:
    print("accepted")
else:
    print("not accepted")

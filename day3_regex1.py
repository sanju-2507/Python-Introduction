
import re

a= "hello friends, pain in spain !!"
b= "good evening 123 867 everyone "

x= re.search("^h.*!$" , a)

if x:
    print(x)

else: 
    print("wrong data")


#another 
x1= re.findall("[a-m]", a)
print("x1 : ",x1)

x2= re.findall("\d",b)
print(x2)

x3= re.findall("he..o",a)
print(x3)

x4= re.findall("^good", b)
if x4:
    print("correct")
else:
    print("wrong")

x5= re.findall("everyone $", b)
if x5:
    print("correct")
else:
    print("wrong")


txt1= "too much rain "
z1=re.findall("[l-z]", txt1)
print(z1)
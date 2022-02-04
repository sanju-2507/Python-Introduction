#print 1-10 
i=1
while i<11:
    print(i)
    i=i+1

#print table
i=1
while i<11:
    c=5*i
    print(c)
    print("5 * ",i,"=",c)
    i=i+1

#print table and take number from user

a = int(input("Enter a Number: "))
b=1
while b<11:
    d=a*b
    print(b, "*",a,"=",d)
    b=b+1 


#print table and take number from user

a = int(input("Enter a Number: "))
b=1
while b<11:
    d=a*b
    print("%d * %d = %d" %(a,b,d))
    b=b+1 


#while with break 

a=1
while a<11:
    print(a)
    a=a+1
    if(a==5):
        break

else:
    print("Finished")


#if else

a=122
b=24

if(a<b):
    print(b, " is greater and ", a , "is smaller ")
else:
    print(a, "is greater and" ,b,"is smaller")



#elif

a=100
b=120
c=160
if(a>b and a>c):
    print(a)
elif(b>a and b>c):
    print(b)
else:
    print(c)



#break

for i in "Mango":
    if i=='n':
        break
    print(i)


#break examples

i=0
while 1:
    print(i, " ",end=" ")
    i=i+1

    if i==7:
        break;
print("End loop")


#another table example

n=5
while 1:
    i=1
    while i<11:
        c=n*i
        print(n,"*",i,"=",c)
        i=i+1

    choice= int(input("Do you want to continue printing table or press 0 for stop: "))
    if choice == 0:
        break;
    n=n+1


#continue

i=0
while i<10:
    i = i+1
    if(i==5):
        continue;
    print(i)
print("finished")


#continue another example

st="whats up friends"
for i in st:
    if i=='p':
        continue;
    print(i)



#pass

for i in range(1,11):
    if i==5:
        pass
        print("pass ",i)
    print(i)

#another example on pass

for i in "apple":
    pass
    print(i)

    
       
        
    

#abs() 

a=-101
b=-50.39
c= -5j
d= -4+10j

print(abs(a))
print(abs(b))
print(abs(c))
print(abs(d))


#all()

e=[1,2,3,4,'ab', 'sds', 19.92, 12.0]
print(all(e))
e1=[1,2,3,4,'ab', 0, 19.92, 12.0]
print(all(e1))
e2=[1,2,3,4,'ab', 'sds', False, 12.0]
print(all(e2))
e3=[1,2,3,4,True, 'sds', 19.92, 12.0]
print(all(e3))
e4=[False, True]
print(all(e4))
e5=[True, False]
print(all(e5))


#bin() function

f=10
print(bin(f))

f1= 20
f2= bin(f1)
print(f2)

print(bin(45))



#lambda function !!!

x= lambda a: a+50
print("Addition of two number is : ",x(20))
print(x)
print(type(x))

x1= lambda a,b: a*b*10
print("Multiplication is : ",x1(4,6))


#lambda with filter

list0= [12,23,3,4,45,56,67,78,88]
x3= list(filter(lambda x: x%2==0,list0))
print(x3)

list1=['a', 'v','e', 'd', 'r','e']
x4= list(filter(lambda x: x!='e', list1))
print(x4)


#lambda with map

list2= [1,2,3,4,5,6,7,8,9]
sq= list(map(lambda x: x**2,list2))
print(sq)

list3 = [1,2,3,4,5,6]
sqr= list(map(lambda x,y: x*y*10,list3,list3))
print(sqr)

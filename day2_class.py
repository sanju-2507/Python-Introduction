#class !!!

from time import process_time_ns
from unicodedata import name


class Employee:
    id = 10
    name = 'abc'

    def dis(self):
        print("Id: %d\nName: %s\n" %(self.id, self.name))

e1= Employee()
e1.dis()



class Test:
    """Hello today is your test !!!"""
    id = 10
    name = 'pqr'

    def display(self):
        print(self.id)
        print(self.name)

    def show(self):
        print(self.na)

t1= Test()
t2 = Test()

t1.display()
t2.na = 'ahfjahf'
t2.show()
print(Test.__doc__)

#examples

class Child:
    leave = 10
    pass

a=Child()
a.name = 'abc'
a.age=10
a.city= 'indore'

print(a)
print(a.name)
print(a.leave)
print(a.__dict__)
print(Child.__dict__)
leave = 20
print(a.leave)
print(Child.leave)



#another example 

class Human:
    def __init__(self,n,a):
        self.name = n
        self.age= a

    def show(self):
        if self.age>20:
            print("you can drive ",self.name)
        else:
            print(self.name, "You cannot drive")

tom=Human('sam', 30)
tt=Human('tt',15)
tom.show()
tt.show()




#abstract class and method 

from abc import ABC, abstractmethod

class Computer(ABC):

    @abstractmethod
    def process(self):
        print("hello computer !!!")

class Laptop(Computer):

    def process(self):
        print("hello Laptop !!!")

l1= Laptop()
l1.process()



#abstract class and method  another examples

from abc import ABC, abstractmethod

class Computer(ABC):

    @abstractmethod
    def process(self):
        print("hello computer !!!")

    def show(self):
        print("self self")

class Laptop(Computer):

    def process(self):
        print("hello Laptop !!!")

l1= Laptop()
l1.process()



#abstract class and method  another examples

from abc import ABC, abstractmethod

class Computer(ABC):

    @abstractmethod
    def process(self):
        print("hello computer !!!")


        
from abc import ABC, abstractmethod
 
class Polygon(ABC):
 
    @abstractmethod
    def noofsides(self):
        pass

    def display(self):
        print("whats up ")
 
class Triangle(Polygon):
 
    # overriding abstract method
    def noofsides(self):
        print("I have 3 sides")

    def show(self):
        print("hello hii all")
 
class Pentagon(Polygon):
 
    # overriding abstract method
    def noofsides(self):
        print("I have 5 sides")
 
class Hexagon(Polygon):
 
    # overriding abstract method
    def noofsides(self):
        print("I have 6 sides")
 
class Quadrilateral(Polygon):
 
    # overriding abstract method
    def noofsides(self):
        print("I have 4 sides")
 
# Driver code

R = Triangle()
R.noofsides()
R.show()
 
K = Quadrilateral()
K.noofsides()
 
R = Pentagon()
R.noofsides()
 
K = Hexagon()
K.noofsides()



from abc import ABC, abstractmethod
 
class Polygon(ABC):
 
    @abstractmethod
    def noofsides(self):
        pass
 
class Triangle(Polygon):
 
    # overriding abstract method
    def noofsides(self):
        print("I have 3 sides")
 
class Pentagon(Polygon):
 
    # overriding abstract method
    def noofsides(self):
        print("I have 5 sides")
 
class Hexagon(ABC):
 
    # overriding abstract method
    def noofsides(self):
        print("I have 6 sides")
 

 
# Driver code
R = Triangle()
R.noofsides()
 
R = Pentagon()
R.noofsides()
 
K = Hexagon()
K.noofsides()



from abc import ABC, abstractmethod
class Test(ABC):
      @abstractmethod
      def m1(self):
          pass
      @abstractmethod
      def m2(self):
          pass

class SubTest(Test):
    def m1(self):
        print("m1 method")

    def m2(self):
        pass

s=SubTest()
s.m1()

from abc import ABC, abstractmethod
class Test(ABC):
      @abstractmethod
      def m1(self):
          pass
      @abstractmethod
      def m2(self):
          pass

class SubTest(Test):
    def m1(self):
        print("m1 method implementation")

    def m2(self):
        print("m2 method implementation")

s=SubTest()
s.m1()
s.m2()
print(s.__dir__)
print(s.m1.__dir__)
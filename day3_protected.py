#protected variables 

class Student:
    def __init__(self,n,a,c):
        self._name=n
        self._age=a
        self._city=c

    def _show(self):
        print("Name: %s\nAge: %d\nCity: %s\n "%(self._name, self._age, self._city))

class Test(Student):
    def __init__(self, n, a, c):
        super().__init__(n, a, c)


    def display(self):
        print("public class")

        self._show()

t1=Test('abcd', 10, 'indore')
t1.display()





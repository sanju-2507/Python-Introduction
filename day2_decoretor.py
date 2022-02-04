#decorator !!!

def func1(msg):
    print(msg)

func1("hii")

func2=func1
func2("hello")

#inner function

def fun():
    print("hello ")

    def fun1():
        print("hiiii")

    def fun2():
        print("how are you ")

    fun1()
    fun2()

fun()


#higher function

def add(x):
    return x+10
def sub(x):
    return x-10

def operator(f, x):
    temp= f(x)
    return temp

print(operator(add,40))
print(operator(sub,90))


#decorating function with parameters

def divide(x,y):
    print(x/y)
def outer(func):
    def inner(x,y):
        if x<y:
            x,y=y,x
            return func(x,y)
    return inner
d1= outer(divide)
divide(7,40)

#funtion with no arguments:

def print_something():
    print("hello world")
print_something()

#function with arguments

def print_something(text):
    print(text)
print_something("Hello, world!")

#3
def greet(name):
    print("Hello , My name is " + name)
greet("Susan")
greet("Nigel")

#4,
def addition(int1,int2):
    return int1 +int2
print(addition(2,2))

#5
def addition(int1=2,int2=2):
    return int1 + int2
#print(addition())
print((addition(4,4))) #  when we provide arguments, python ignores the defaults and use our values instead.

#6
def print_every_number(*numbers):# * indicate it accepts any numbers of arguments ,and it save as a tuple
    print(type(numbers))
    for numbers in numbers:
        print(numbers)
print_every_number(1,2,2,3,5,6,6)

#7

def greeting(name: str):
    print(type(name)) # it shows class int. it doesn't convert the value to a string. python still uses whatever type you passed.
    print("Hello", name)
greeting(2323232)

#8
def division(a :int=2,b: int=5):
    return a/b
a: int=4
b: int=6
print(division(a,b))
print(division())

# functions names should clearly describe what the function does (add, sub..)
#use lowercase letters with underscore if its needed
#each function should do one things .
#make it easy to understand what types are expected and returned.
#use return values from functions instead of printing

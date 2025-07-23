def add(a,b):
    return a+b
print(add(a=2,b=3))

def sub(a,b):
    return a-b
print(sub(5,3))

def multiply(a,b):
    return a*b
print(multiply(8,9))

def div(a,b):
    return a/b
print(div(8,2))

# calculator.py

# calculator.py
#
# def add(a, b):
#     return a + b
#
# def subtract(a, b):
#     return a - b
#
# def multiply(a, b):
#     return a * b
#
# def divide(a, b):
#     if b == 0:
#         return "Error: Division by zero!"
#     return a / b
#
# # All the logic directly in the script
# print("Welcome to Mini Calculator!")
# print("Operations: +, -, *, /")
#
# try:
#     a = float(input("Enter first number: "))
#     op = input("Enter operation (+, -, *, /): ")
#     b = float(input("Enter second number: "))
# except ValueError: #We use try-except ValueError to catch mistake when user enter the wrong data type,it will give message . (ex instead of int if user enter str value)
#     print("Invalid input, please enter numbers.")
# else:       #-if the user has input the right data type then it will continue with the next step
#     if op == '+':
#         result = add(a, b)
#     elif op == '-':
#         result = subtract(a, b)
#     elif op == '*':
#         result = multiply(a, b)
#     elif op == '/':
#         result = divide(a, b)
#     else:
#         result = "Invalid operation!"
#
#     print(f"Result: {result}")
#
#

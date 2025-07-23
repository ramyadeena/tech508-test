
# from jsonfile.parse_json_to_dict import value


# def is_even(num):
#     if num % 2 == 0 :
#         return True
#     else:
#         return False
# print(is_even(10))
# print(is_even(23)
# )

# Create a function `calculator(a, b, operation)` that performs addition, subtraction,
# multiplication, or division based on the `operation` parameter ('add', 'sub', 'mul', 'div').

# def add(a,b):
#     return a+b
# print(add(3,4))
# def sub(a,b):
#     return a-b
# print(sub(7,6))
#
# def mul(a,b):
#     return a * b
# print(mul(8,7))
#
# def div(a,b):
#     return a /b
# print(div(18,6))

# a = int(input("enter the number: "))
# b= int(input("enter the number: "))
# op = input("enter the following opertion : (+,-,*,%) " )
#
# if op == "+":
#     print(a + b)
# elif op == "-" :
#     print(a-b)
# elif op == "*":
#     print( a*b)
# else:
#     op == "/"
#     print(a/b)

# # Define a function `sum_list(lst)` that returns the sum of all elements in a list.
# def sum_list(list):
#     total=0
#     for num in list:
#         total += num
#     return total
#
# print(sum_list([1,3,3,4,4,4]))

# def big_number(a,b,c):
#     if (a > b) & (a > c):
#         return ("a is greater")
#     elif (b >a) & (b > c):
#         return ("b is greater")
#     else:
#         return ("c is greater")
#
# print(big_number(12,34,56))

# Define a function `count_vowels(s)` that returns the number of vowels (a, e, i, o, u) in a string.

def count_vowels(param):
    vowels = ("a","e","i","o","u")
    for char in param:
     if char in vowels:
        return ("yes vowels is found")
    else:
        return("no vowels")

print(count_vowels("apple"))
print(count_vowels("ttydd"))











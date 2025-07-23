# Mini-calculator
from math_operation import *
import math_operation # then you have to put math_operation.add

from math_operation import mul

first_num = int(input("Enter the first number: "))
second_num = int(input("Enter the first number: "))
result = mul(first_num, second_num)
#print(f"{first_num} + {second_num} = {result}")
print(result)
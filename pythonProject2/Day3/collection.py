# from idlelib.replace import replace
#
# shopping_list =['egg','bread','bananas','biscuits','milk']
# print(shopping_list)
#
# #print data type :
# print(type(shopping_list))
#
# #print first item on the list:
# print(shopping_list[0])
#
# #print last item on the list:
# print(shopping_list[-1])
#
# #change the second item in the list to rice
# shopping_list[1]='rice'
# print(shopping_list)
#
# #add the time in the list
# shopping_list.append('carrot') # add item to the list
# print(shopping_list)
#
# #add another list of two item to the shopping_list
# another_list =['coffee','toffee']
# print(another_list)
# shopping_list.extend(another_list) # extend command add the another list to the current list
# print(shopping_list)
#
# #remove banana from the list
# shopping_list.pop(2) # we can use pop(index) to remove the item from the list
# print(shopping_list)
#
# #or
# shopping_list.remove('coffee')
# print(shopping_list)
#
# for i in range(1, 5):
#     print(i)
# else:
#     print("this is else block statement" )
#
# salary = 8000
#
# def printSalary():
#     salary = 12000
#     print("Salary:", salary)
# printSalary()
# print("Salary:", salary)
#
# sampleSet = {"Jodi", "Eric", "Garry"}
# sampleSet.add("Vicki")
# print(sampleSet)
#
# listOne = [20, 40, 60, 80]
# listTwo = [20, 40, 60, 80]
#
# print(listOne == listTwo)
# print(listOne is listTwo)
#
# def calculate (num1, num2=4):
#   res = num1 * num2
#   print(res)
#
# calculate(5, 6)
#
# var= "James Bond"
# print(var[2::-1])
#
# text = "hello world"
# parts = text.split(" ")
# print(parts[0])
#
# print(type(range(5)))
#
# my_dict = {"a": 1, "b": 2}
# my_dict["c"] = 3
# my_dict["a"] = 10
# print(my_dict["a"])

#
# def func():
#     #global value
#     value = "Local"
#
#
# value = "Global"
# func()
# print(value)
#
# def solve(a, b):
#    return b if a == 0 else solve(b % a, a)
# print(solve(20, 50))
#
# count = 0
# while(True):
#    if count % 3 == 0:
#        print(count, end = " ")
#    if(count > 15):
#        break;
#    count += 1
#
#
# a = [[], "abc", [0], 1, 0]
# print(list(filter(bool, a)))
#
# numbers = (4, 7, 19, 2, 89, 45, 72, 22)
# sorted_numbers = sorted(numbers)
# even = lambda a: a % 2 == 0
# even_numbers = filter(even, sorted_numbers)
# print(type(even_numbers))

print(36 / 4)
a = [10, 20]
b = a
b += [30, 40]
print(a)
print(b)
print(bool(0))
print(bool(""))
print(bool([1]))

x = 10
y = 3
print(x // y)

print(2 % 6)

print(2 * 2 ** 2 * 2)
a = "Python"
b = "3"
print(a + b * 2)

b="3"
print(b * 3)
message = "Hello"
print('e' in message)
print('x' in message)

x = [1, 2, 3]
y = [1, 2, 3]
print(x == y)
print(x is y)

x = 10
y = 50
if x ** 2 > 100 and y < 100:
    print(x, y)


print('[%c]' % 65)

print('Mike', 'Sydney', sep='**')

print('%x, %X' % (15, 15))

print("Line 1", end="***")
print("Line 2")

aList = [5, 10, 15, 25]
print(aList[::-2])

my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(my_list[:4])
print((my_list[::-1]))
print((my_list[1::2]))
print(my_list[-3:])
print(my_list[::-2])

nested_list = [[1, 2], [3, 4], [5, 6]]
print(nested_list[1][1])

letters = ['a', 'b', 'c', 'd', 'e']
letters[1:4] = ['x', 'y']
print(letters)

sampleList = [10, 20, 30, 40]
sampleList =[]

sampleList = [10, 20, 30, 40, 50]
sampleList.append(60)
print(sampleList)

sampleList.append(60)
print(sampleList)

my_list = [1, 2, 3]
my_list.append([4, 5])
print(len(my_list))


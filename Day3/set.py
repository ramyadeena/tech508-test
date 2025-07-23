#explain 2 main way the set are different from lists and tuple
#  A set is a collection which is unordered, unchangeable, and unindexed.
#Set: Cannot contain duplicate values. List/Tuple: Can contain duplicates.

set={"apple","banana","cherry"}
print(set)
print(type(set))

#add orange to the set
set.add("orange")
print(set)

#remove banana to the set
set.remove("banana")
print(set)

#add another apple to the set
set.add("apple")
print(set) # it wont allow duplicate value

#print 2nd item in the set.
#we cannot print 2nd item in the set because set is unindexed. we cannot access through index like how we do in list
#we use loop to print the item

set1 = {"blue","red","orange","violet"}
list1=["white","orange","black"]
set1.update(list1)
print(set1)

set1 = {"blue","red","orange","violet"}
tuple1 = ("white","violet")
set1.update(tuple1)
print(set1)
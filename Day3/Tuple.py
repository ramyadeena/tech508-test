#how are tuples similiar to lists?
#A tuple is an ordered collection of elements, often referred to as items, that can contain different types of data. it is similar to list

#Are tuples immutable and what does this mean?
#but unlike lists, tuples are immutable, meaning they cannot be modified once created.

# what other data types are immutable?
#string and tuple are immutable.

#what are the good use case for tuples instead of lists?
#You should use a tuple instead of a list when you have a collection of items that should not be modified

essentials =("Tent","books","phone")
print(essentials)
print(essentials.count("bread"))


#----------task

print("You are stranded on a desert island. You can take only THREE items.")
essential_item1 = input("What is an essential item you would take? ")
essential_item2 = input("What is an essential item you would take? ")
essential_item3 = input("What is an essential item you would take? ")
essentials_tuple = (essential_item1,essential_item2,essential_item3)
print(essentials_tuple)
print("Here are your items as a tuple:", essentials_tuple)
print("")
print("I lied. You can take one more item.")
essential_item4 = input("What is one more essential item you would take? ")
essentials_tuple = essentials_tuple +(essential_item4,) # -- to add the item in tuple we should put comma at the end otherwise it think as regular value not tuple.
print("Here are your items as a tuple:", essentials_tuple )



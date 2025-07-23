# what dictionary?
# A dictionary in Python stores data as key-value pairs. It is an unordered, changeable, and indexed collection.
#what does each value need to be accompanied/associated with?
#each value is associated with key value pair.it can be of any data type, (string, int, list..)

# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
# Dictionary is a collection which is ordered** and changeable. No duplicate members.


student_1 = {
    "name":"Susan",
    "stream" :"tech",
    "completed_lessons": 4,
    "completed_lessons_names" :["variable","data_types","set"]

}
print(student_1)

#print data type to the screen
print(type(student_1))

# print the value of keyvalue pair having the key stream
print(student_1["stream"])

#print the value for completed lesson names check you can see the list of 3 items.
print(student_1["completed_lessons_names"])

#print data type for the value for completed lesson names -check it is a list.
print(type(student_1["completed_lessons_names"]))

#print the first element in the list of completed lesson names.
print(student_1["completed_lessons_names"][0])

# change the value of completed lesson to 3 (an integer not an string)
student_1["completed_lessons"]=3
print(student_1)
print(type(student_1["completed_lessons"]))

# delete data_types from the list.
#student_1.pop("data_types")--- trying to remove the string so showed error.
#print(student_1)

student_1["completed_lessons_names"].remove("data_types")
print(student_1)

#list all the keys

print(student_1.keys())

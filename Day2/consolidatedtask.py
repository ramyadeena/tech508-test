# Consolidation Task: Improve on previous task to capture user details
# Improve on the task where you captured the name, DOB and age of the user and printed them to the screen
# Now ask for user for the details show below and produce the output as shown.
# In the process, you should:
# Convert the age inputted to a integer
# Use concatenation so that you are forced to convert the age back to a string (or use an alternative method than concatentation or f-strings so that you you don't need to convert back to a string)
# # Use an f-string at least once
name = input("My name is : ")
age = int(input("My age is : "))
month = input("what month were you born: ")
year = input("What year were you born: ")
print(f"Hi {name}, {age}")
print(f"You are born in {month} of the year {year}")
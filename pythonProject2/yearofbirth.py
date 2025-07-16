from datetime import datetime

from fstring import years

age_int = 18
name = "Swetha"
current_year = datetime.now().year
print(current_year)
yearofbirth = current_year-age_int
print(yearofbirth)
print(f"OMG,{name},you are {age_int} years old so you were born in year {yearofbirth}")

#--------------------------------------------
age=int(input("Enter your age: "))
name= input("Enter your name: ")
current_year=datetime.now().year
print(current_year)
yearofbirth=current_year-age
print(yearofbirth)
print(f"OMG,{name},you are {age_int} years old so you were born in year {yearofbirth}")

#calculate and print out the total number of hours this person has lived


age_int = 62
name = "Angel"
current_year = datetime.now().year
print(current_year)
yearofbirth = current_year-age_int
print(yearofbirth)
days_lived = age_int*365*24
hours_lived=age_int*365*24*60
print(f"{name} has lived for {days_lived} days")
print(hours_lived)

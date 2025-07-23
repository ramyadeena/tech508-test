# age = int(input("What is your age? "))
# print(f" Your age is  {age}")

user_prompt = True

while user_prompt:
    age = input("Whats is your age?" )
    if age.isdigit() and int(age) < 117 :
        user_prompt = False
    else:
        print("please enter your age using digits.")
print(f" your age is {age}")
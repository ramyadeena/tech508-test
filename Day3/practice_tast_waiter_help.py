print("Welcome to the restarunt")

starters = ["soup","Nuggets","paneer65","cheesebites"]
user = input("What do you like to have for starters: ")
main=["Briyani","chickenwrap","grillchicken","halloumiwrap","burger"]
user_1=input("What do you like to have for mains: ")
desserts = ["vanilla icecream","gulabjamun","halwa","chocolatecake","carrotcake","kulfi"]
user_2=input("what do you like to have for desserts: ")
customer_order_list =[user,user_1,user_2]
print(customer_order_list)
print(f"You have ordered: ")
print(f"Starters: {user}")
print(f"Main: {user_1}")
print(f"Dessert: {user_2}")
print(f"Your complete ordered list : {customer_order_list}")
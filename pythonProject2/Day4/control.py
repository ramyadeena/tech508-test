# possible film ratings are "universal", "pg", "12", "12a", "15", "18"
# film_rating =input("Enter the film rating (universal,pg,12,12a,15,18):").lower()
#
# if film_rating == "universal":
#     print("all age groups can watch this film")
#
# elif film_rating =="pg":
#     print("General viewing, but some scenes may be unsuitable for young children.")
#
# elif film_rating =="12" or film_rating=="12a":
#     print("Films classified 12A and video works classified 12 contain material that is not generally suitable for children aged under 12. No one younger than 12 may see a 12A film in a cinema unless accompanied by an adult.")
# elif film_rating =="15":
#     print("No one younger than 15 may see a 15 film in a cinema.")
# elif film_rating=="18":
#     print("No one younger than 18 may see an 18 film in a cinema.")
# else:
#     print("This is not a correct rating, please use universal, pg, 12, 12a, 15, 18")

list = [i for i in range(1,6,2)]
print(list)

prices = {"apple": 1.2, "banana": 0.5, "orange": 0.8}
quantities = {"apple": 3, "banana": 5, "orange": 2}
total = sum([prices.get(key, 0) * quantities.get(key, 0) for key in prices])
print(total)

# Nested dictionaries
sales = {
    'store1': {'jan': 1000, 'feb': 1200},
    'store2': {'jan': 800, 'feb': 900}
}
for item in sales.values():
    for item in item.keys():
        print(item)

def is_palindrome(param):
    return param == param[::-1]

print(is_palindrome("madam"))

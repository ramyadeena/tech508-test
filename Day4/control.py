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
# #     print("This is not a correct rating, please use universal, pg, 12, 12a, 15, 18")
# #
# # list = [i for i in range(1,6,2)]
# # print(list)
# #
# # prices = {"apple": 1.2, "banana": 0.5, "orange": 0.8}
# # quantities = {"apple": 3, "banana": 5, "orange": 2}
# # total = sum([prices.get(key, 0) * quantities.get(key, 0) for key in prices])
# # print(total)
#
# # Nested dictionaries
# sales = {
#     'store1': {'jan': 1000, 'feb': 1200},
#     'store2': {'jan': 800, 'feb': 900}
# }
# for item in sales.values():
#     for item in item.keys():
#         print(item)
#
# def is_palindrome(param):
#     return param == param[::-1]
#
# print(is_palindrome("madam"))
#
#
# def second_largest(numbers):
#     unique_numbers = list(set(numbers))
#     unique_numbers.sort()
#     if len(unique_numbers) < 2:
#         return None  # or raise an exception
#     return unique_numbers[-2]
# print(second_largest([3,6,12,2,45]))
from pythonProject2.Day3.collection import my_list
# from pythonProject2.jsonfile.parse_json_str_to_dict import value

# my_dict = {'name': 'Alice', 'age': 35, 'city': 'New York'}
# my_dict["profession"] ="doctor"
# print(my_dict)
# my_dict['age']= 40
# print(my_dict)
# print(my_dict["city"])
#
# my_dict = {'name': 'Alice', 'age': 35, 'city': 'New York', 'profession': 'Doctor'}
# my_dict.pop("profession")
# print(my_dict)
# for key,value in my_dict:
#     print(key,value)
#
# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]
# final = dict(zip(keys,values))
# print(final
#
# my_dict = {'name': 'Alice', 'age': 35, 'city': 'New York'}
# my_dict.clear()
# print(my_dict)
#
# dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
# dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
# dict1.update(dict2)
# print(dict1)
#
# data = {'person': {'name': 'Alice', 'age': 30}}
# for key,value in data.items():
#     for inner_key,inner_value in value.items():
#         print(inner_key,inner_value)
sampleDict = {
    "class": {
        "student": {
            "name": "Mike",
            "marks": {
                "physics": 70,
                "history": 80
            }
        }
    }
}
for key,value in sampleDict.items():
    for inner_key ,inner_value in value.items():
        for inner_key,inner_value in value.items():
            for inner_key,inner_value in value.items():
                print(inner_value)
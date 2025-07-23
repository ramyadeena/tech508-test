# list_data = [1, 2, 3, 4, 5]
# embedded_lists = [[1,2,3],[4,5,6]]
dict_data = {1: {"name": "Bronson", "money": "$0.05"}, 2: {"name": "Masha", "money": "$3.66"}, 3: {"name": "Roscoe", "money": "$1.14"}}
#
# list_data = [1, 2, 3, 4, 5]
# squared_list =[]
# for num in list_data:
#     squared_list.append(num * num)
#     num =num+1
# print(squared_list)
#
#
# embedded_lists = [[1,2,3],[4,5,6]]
#
# for data in embedded_lists:
#     print(data)
#
# for data in embedded_lists:
#     print(data)
#     for inner_list in data:
#         print(inner_list)
#
# dict_data = {1: {"name": "Bronson", "money": "$0.05"}, 2: {"name": "Masha", "money": "$3.66"}, 3: {"name": "Roscoe", "money": "$1.14"}}
#
# for keys in dict_data:
#     print(keys)
#
# for value in dict_data.values():
#     print(value)
#
for items in dict_data.values():
    for items in items.values():
        print(items)

#
# for key,value in dict_data.items():
#     print(value["money"])
#
#
# list_data = [1, 2, 3, 4, 5]
# for item in list_data:
#     if item < 3 :
#         print("less than 3")
#     elif item == 3:
#         print("i found 3")
#     else:
#         print("greater than 3")
#    # print(item)

for item in dict_data.values():
    print(item["money"])

    numbers = (4, 7, 19, 2, 89, 45, 72, 22)
    sorted_numbers = sorted(numbers)
    print(sorted_numbers)
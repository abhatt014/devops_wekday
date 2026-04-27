# fruits = ["apple", "banana", "cherry"]
# print(fruits)  # Output: apple
# for f in fruits:
#     print(f)


# for i in range(5):      # 0, 1, 2, 3, 4
#     print(i)
# print("*************************")

# for i in range(2, 6):   # 2, 3, 4, 5
#     print(i)
# print("*************************")
# for i in range(0, 10, 2): # 0, 2, 4, 6, 8
#     print(i)


my_dict = {
    'name': 'Alice', 
    'age': 30, 
    'city': 'New York'
    }

for key in my_dict:
	value = my_dict[key]
	print(f"{key}: {value}")


# for i in my_dict:
#     print(i)  # Output: name, age, city (keys)
# for key,value in my_dict.items():
#     print(f"{key}: {value}")  # Output: name Alice, age 30, city New York (key-value pairs)    
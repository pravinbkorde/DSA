# def print_items(n):
#     for i in range(n):
#         print(i,end=" ")
# n = 10
# print_items(n)

# def print_items(n):
#     for i in range(n):
#         for j in range(n):
#             print(i,j)
#
# print_items(10)

# def add_items(n):
#     return n+n+n
# print(add_items(5))


# num1 = 11
# num2 = num1
# print(f"Value of num1 is {num1}")
# print(f"Value of num2 is {num2}")
#
# print(f"Memory location of num1: {id(num1)} ")
# print(f"Memory location of num2: {id(num2)} ")
#
# print(f"--------------After changing the value-------------------")
# num2 = 22
# print(f"Value of num1 is {num1}")
# print(f"Value of num2 is {num2}")
#
# print(f"Memory location of num1: {id(num1)} ")
# print(f"Memory location of num2: {id(num2)} ")


# dict1 = {
#     "value":11
# }
# dict2 = dict1
# print(f"Value of dict1: {dict1}")
# print(f"Value of dict2: {dict2}")
# print(f"Memory location of dict1: {id(dict1)}")
# print(f"Memory location of dict2: {id(dict2)}")
# print(f"--------after changing the value-------------")
# dict2["value"] = 55
# print(f"Value of dict1: {dict1}")
# print(f"Value of dict2: {dict2}")
# print(f"Memory location of dict1: {id(dict1)}")
# print(f"Memory location of dict2: {id(dict2)}")

head = {
    "value":11,
    "next":{
            "value":12,
            "next":{
                    "value":22,
                    "next":{
                        "value":55,
                        "next":{
                                "value":44, #----------------> Tail
                                "next":None
                        }                                               
                }
            }
    }
}

print(head["next"]["next"]["value"])























list1 = ["apple", "banana", "cherry"]

dict1 = {
    # Key value pairs
    10: "apple",
    20: "banana",
    30: "cherry",
    30: "kiwi",
    40: ["date", "elderberry", "fig"],
    50: (1, 2, 3),
    60: {"name": "grape", "color": "purple"}
}

# dict2 = dict1

# dict2[70] = "honeydew"

# print(dict1)
# print(dict2) 

dict2 = dict1.copy() 

dict2[70] = "honeydew"

print(dict2.get(80, "Not Found")) 

# [(10, "apple"), (20, "banana"), (30, "kiwi"), (40, ["date", "elderberry", "fig"]), (50, (1, 2, 3)), (60, {"name": "grape", "color": "purple"})]

# print(dict1)
# print(dict2) 

# print(dict1[60]["color"]) 


# name -> fname, lname, surname

name = {
    "fname": "John",
    "lname": "Doe",
    "surname": "Smith"
}

# age -> age
# address -> street, city, state

address = dict(street="123 Main St", city="Anytown", state="CA") 

# print(address.keys())
# print(address.values()) 

# address["city"] = "Othertown"

# address["pincode"] = "12345"

# address.pop("city")

# address.popitem()

# print(address)
# print(address.items())

# if "city" in address:
#     print("City is present in the address dictionary.")
# else:
#     print("City is not present in the address dictionary.")

# phone -> country_code, number 

# print(len(dict1))

# print(dict1[10]) 
# print(dict1[20]) 
# print(dict1[30]) 
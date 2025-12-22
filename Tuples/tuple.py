# Packing Values in a tuple
myTuple = ("mango", "kiwi", "apple", "mango")

print(myTuple.count("mango"))

a = myTuple * 3
print(a)

# Unpacking Tuples
(yellow, green, red, yellow) = myTuple

print(green)  

tuple1 = ("example1",)

tuple_to_list = list(myTuple) 

# print(type(tuple_to_list))

tuple_to_list[2] = "banana"

# print(tuple_to_list)

# print(myTuple[2:4])
# print(type(tuple1)) 
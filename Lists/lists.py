# list -> used to hold multiple values in a single variable


#          0    1   2
numbers = [10, 20, 30, "Hello"] 
age = [21, 23, 0, 10, 25, 27, 21] 

numbers[1] = 35
print(numbers)

age.sort(reverse=True)
print(age)

res = age.count(21) 
# print(res)

# print(numbers) 
# print(numbers[2]) 

numbers.append(40)
numbers.append(50)

# numbers.append(age)

numbers.extend(age) 

print(numbers.index("Hello")) 

numbers.insert(2, "Mango") 

numbers.pop()
numbers.pop()
numbers.pop()
numbers.pop(2)

numbers.reverse()

# age.clear()

numbers_copy = numbers.copy() 
# print(numbers_copy)

# print(age)

print(numbers)
print(numbers[7]) 
# print(numbers[5] + 2)  
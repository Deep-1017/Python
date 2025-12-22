# Count Digits in a Number 

number = 53219456123486313
count = 0

while number != 0:
    number = number // 10 
    count += 1
print("Number of digits in the given number is:", count)
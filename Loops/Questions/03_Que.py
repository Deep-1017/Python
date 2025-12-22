# Reverse a Number 

number = 1234             
reverse_number = 0

while number != 0: 
    rem = number % 10    
    reverse_number = (reverse_number * 10) + rem 
    number = number // 10 
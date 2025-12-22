# num1 = 23
# num2 = 12
# num3 = num1 + num2
# print(num3)

# num4 = 54
# num5 = 56
# num6 = num4 + num5
# print(num6) 


# Python Functions 

# Function Definition
def addition(a, b, c = 10):
    res = a + b + c
    print(res)
    # return a + b + c

def greet():
    pass

# Function Call
# addition(23, 12, 50) 
# addition(54, 56)
# addition(100, 200)  



fruits = ['Mango', 'Banana', 'Orange', 'Grapes']
cities = ['New York', 'London', 'Mumbai', 'Tokyo']


def show_fruits(fruit_list):
    for fruit in fruit_list:
        print(fruit)

# show_fruits(fruits) 
# show_fruits(cities) 


# Python Scope
    # 1) Local Scope
    # 2) Global Scope

# Global Variable
a = 100

def func1():
    global x
    x = 10
    print(x)
    print(a)

# print(x)
# print(a) 

    

# Lambda Function
sum = lambda a, b, c, d, e : a + b + c + d + e
# print(sum(10, 20, 30, 40, 50)) 


def multiply(x):
    return lambda a : a * x 

double = multiply(2)
print(double(45)) 
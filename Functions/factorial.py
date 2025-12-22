# 5! = 5 * 4 * 3 * 2 * 1 = 120 
# 5! = 5 * 4!

# n! = n * (n-1)!

# 1! = 1 
# 0! = 1  

def fact(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fact(n - 1)
    
res = fact(5) 
print(res)  

# 5 * fact(4)
# 5 * 4 * fact(3)
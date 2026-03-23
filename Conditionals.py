# Operators in Python
# AND operator 
2 > 1 and 3 > 2 # True

# Equality operator
1 == 1 # True

# NOT operator
not (2 > 1) # False

# OR operator
2 > 1 or 3 < 2 # True

# IF - ELIF - ELSE statement
x = 10

if x > 10:
    print("x is greater than 10")
elif x == 10:
    print("x is equal to 10")   
else:
    print("x is less than 10")

# Dictionary membership operator    
'key' in {'key': 'value'} # True
'key' in {'key': 'value'}.keys() # True
'value' in {'key': 'value'}.values() # True 

# List membership operator
3 in [1, 2, 3] # True
5 not in [1, 2, 3] # True

# Set membership operator
'a' in {'a', 'b', 'c'} # True

# Tuple membership operator
2 in (1, 2, 3) # True
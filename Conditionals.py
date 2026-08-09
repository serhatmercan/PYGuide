# Operators in Python
# AND operator
2 > 1 and 3 > 2 # Output: True

# Equality operator
1 == 1 # Output: True

# NOT operator
not (2 > 1) # Output: False

# OR operator
2 > 1 or 3 < 2 # Output: True

# IF - ELIF - ELSE statement
x = 10

if x > 10:
    print("x is greater than 10")
elif x == 10:
    print("x is equal to 10")
else:
    print("x is less than 10")
# Output: x is equal to 10

# Dictionary membership operator
'key' in {'key': 'value'} # Output: True
'key' in {'key': 'value'}.keys() # Output: True
'value' in {'key': 'value'}.values() # Output: True

# List membership operator
3 in [1, 2, 3] # Output: True
5 not in [1, 2, 3] # Output: True

# Set membership operator
'a' in {'a', 'b', 'c'} # Output: True

# Tuple membership operator
2 in (1, 2, 3) # Output: True
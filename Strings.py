# Commands
# Print a string to the console
print("Hello, World!") # Output: Hello, World!

# Escape characters
# Newline character
print("Hello, \nWorld!") # Output: Hello,
                         #         World!

# Tab character
print("Hello, \tWorld!") # Output: Hello, 	 World!

# Methods
# Capitalize the first letter of a string
"hello, world!".capitalize() # Output: "Hello, world!"

# Count the number of occurrences of a substring in a string
"hello, world!".count("o") # Output: 2

# Accessing characters in a string with indexing
myName = "Serhat"
myName[0] # Output: 'S'
myName[-1] # Output: 't'

# Get the length of a string
len("hello, world!") # Output: 13

# Slicing a string [start:stop:step]
barcode = "ABCDE1234567890"
barcode[5::] # Output : '1234567890' 
barcode[:5:] # Output : 'ABCDE'
barcode[::2] # Output : 'ACE24680'
barcode[3:5] # Output : 'DE'
barcode[1:10:2] # Output : 'BD2468'
barcode[::-1] # Output : '0987654321EDCBA'

# Split a string into a list of substrings
"hello world!".split() # Output : ['hello', 'world!']

# Convert a string to uppercase
"hello, world!".upper() # Output: "HELLO, WORLD!"

# Types
# str -> string
type("Hello, World!")
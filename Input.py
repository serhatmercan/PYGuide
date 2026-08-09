# Reading a line of user input (input() always returns a string)
name = input("Enter your name: ")
# Sample session:
#   Enter your name: Serhat
#   name == 'Serhat'

# === Building a greeting from the input ===
# Three equivalent ways to combine the captured string with other text
print("Hello, " + name + "!")   # Output: Hello, Serhat!
print(f"Hello {name}!")         # Output: Hello Serhat!
print("Hello", name + "!")      # Output: Hello Serhat!

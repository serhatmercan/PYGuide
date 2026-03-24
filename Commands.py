# This is a simple Python program that demonstrates how to use the input() function to get user input and print a greeting message.
name = input("Enter your name: ") # This will prompt the user to enter their name and store it in a variable

print("Hello, " + name + "!") # This will print a greeting with the user's name
print(f"Hello {name}!") # This is another way to print the greeting using an f-string
print("Hello", name + "!") # This is yet another way to print the greeting by separating the string and the variable with a comma
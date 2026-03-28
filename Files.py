# Open a file named "test.txt" in write mode
# This will create the file if it does not exist or overwrite it if it does exist
with open ("test.txt", "w") as file: 
    file.write("Hello, World!") 

# Open the file in read mode
# This will read the content of the file and print it to the console
with open ("test.txt", "r") as file: 
    content = file.read() # Read the content of the file
    print(content) # Print the content to the console    

# Open the file in append mode
# This will add new content to the end of the file without overwriting the existing content
with open ("test.txt", "a") as file: 
    file.write("\nThis is an additional line.")

# Open the file again in read mode to see the updated content
with open ("test.txt", "r") as file: 
    content = file.read() 
    print(content)   
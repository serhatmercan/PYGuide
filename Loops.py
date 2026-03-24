# Break and Continue in For Loop
my_number_list = [1, 2, 3, 4, 5]

for number in my_number_list:
    if number == 3:
        print("Number 3 found, breaking the loop.")
        break
    print(f"Current number: {number}")

for number in my_number_list:
    if number == 3:
        print("Number 3 found, skipping this iteration.")
        continue
    print(f"Current number: {number}")    

# For Loop in Dictionary
my_number_dict = {"a": 1, "b": 2, "c": 3}

for key, value in my_number_dict.items():
    if value % 2 == 0:
        print(f"{key}: {value} is even")
    else:
        print(f"{key}: {value} is odd")

# For Loop in List
my_number_list = [1, 2, 3, 4, 5]

for number in my_number_list:
    if number % 2 == 0:
        print(f"{number} is even")
    else:
        print(f"{number} is odd")

# For Loop in List of Tuples
my_number_tuple_list = [("a", "b"), ("c", "d"), ("e", "f")]        

for (x,y) in my_number_tuple_list:
    print(f"x: {x}, y: {y}")

# For Loop in Set
my_number_set = {1, 2, 3, 4, 5}

for number in my_number_set:
    if number % 2 == 0:
        print(f"{number} is even")
    else:
        print(f"{number} is odd")

# For Loop in Tuple
my_number_tuple = (1, 2, 3, 4, 5)

for number in my_number_tuple:
    if number % 2 == 0:
        print(f"{number} is even")
    else:
        print(f"{number} is odd")        

# While Loop
my_number = 0

while my_number < 5: # This will loop until my_number is less than 5
    print(f"Current number: {my_number}") # This will print the current number before incrementing it
    my_number += 1 # This will increment the value of my_number by 1 in each iteration
# Break and Continue in For Loop
myNumberList = [1, 2, 3, 4, 5]

for number in myNumberList:
    if number == 3:
        print("Number 3 found, breaking the loop.")
        break
    print(f"Current number: {number}")

for number in myNumberList:
    if number == 3:
        print("Number 3 found, skipping this iteration.")
        continue
    print(f"Current number: {number}")    

# For Loop in Dictionary
myNumberDict = {"a": 1, "b": 2, "c": 3}

for key, value in myNumberDict.items():
    if value % 2 == 0:
        print(f"{key}: {value} is even")
    else:
        print(f"{key}: {value} is odd")

# For Loop in List
myNumberList = [1, 2, 3, 4, 5]

for number in myNumberList:
    if number % 2 == 0:
        print(f"{number} is even")
    else:
        print(f"{number} is odd")

# For Loop in List of Tuples
myNumberTupleList = [("a", "b"), ("c", "d"), ("e", "f")]        

for (x,y) in myNumberTupleList:
    print(f"x: {x}, y: {y}")

# For Loop in Set
myNumberSet = {1, 2, 3, 4, 5}

for number in myNumberSet:
    if number % 2 == 0:
        print(f"{number} is even")
    else:
        print(f"{number} is odd")

# For Loop in Tuple
myNumberTuple = (1, 2, 3, 4, 5)

for number in myNumberTuple:
    if number % 2 == 0:
        print(f"{number} is even")
    else:
        print(f"{number} is odd")        
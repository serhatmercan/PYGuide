# Creating an empty dictionary
myDictionary = dict() 

# Definition of the dictionary : Key-Value pairs
fitness_dictionary = {
    "Apple": "100",
    "Banana": "150"
}

# Accessing values in the dictionary
fitness_dictionary["Apple"] # '100'

# Accessing keys in the dictionary
fitness_dictionary.keys() # dict_keys(['Apple', 'Banana'])

# Accessing values in the dictionary
fitness_dictionary.values() # dict_values(['100', '150'])

# Adding a new key-value pair to the dictionary
fitness_dictionary["Orange"] = "200" # Adding a new key-value pair to the dictionary

# Accessing the key-value pairs in the dictionary
fitness_dictionary.get("Apple", 0) # '100' - Accessing the value associated with the key "Apple" using the get() method. If the key does not exist, it will return 0.

# Type of the dictionary
type(fitness_dictionary) # <class 'dict'>
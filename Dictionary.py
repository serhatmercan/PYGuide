# Creating an empty dictionary
my_dictionary = dict() # Output: {}

# Definition of the dictionary : Key-Value pairs
fitness_dictionary = {
    "Apple": "100",
    "Banana": "150"
}

# Accessing values in the dictionary
fitness_dictionary["Apple"] # Output: '100'

# Accessing keys in the dictionary
fitness_dictionary.keys() # Output: dict_keys(['Apple', 'Banana'])

# Accessing values in the dictionary
fitness_dictionary.values() # Output: dict_values(['100', '150'])

# Adding a new key-value pair to the dictionary
fitness_dictionary["Orange"] = "200"

# get() returns a default (here 0) instead of raising KeyError when the key is missing
fitness_dictionary.get("Apple", 0) # Output: '100'

# Type of the dictionary
type(fitness_dictionary) # Output: <class 'dict'>
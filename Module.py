# Importing the serhatmodule to use its functions
import serhatmodule 

# Importing the serhatfunction directly for easier access
from serhatmodule import serhat_function 

# Importing the serhat_subfunction from the serhatsubmodule for direct access
from serhatmodule.serhatsubmodule import serhat_subfunction 

# Calling the serhatfunction using the module name
serhatmodule.serhat_function() 

# Calling the serhatfunction directly without the module name
serhat_function() 

# Calling the serhat_subfunction directly without the module name
serhat_subfunction() 

# __init__.py is a special file in Python that is used to mark a directory as a Python package. 
# It can be empty or contain initialization code for the package. 
# When you import a package, the __init__.py file is executed, allowing you to set up any necessary variables, functions, or classes for the package.
if __name__ == "__main__": # This block will only execute if this script is run directly, not imported as a module
    print("This script is being run directly.")
else: # This block will execute if this script is imported as a module
    print("This script has been imported as a module.")   
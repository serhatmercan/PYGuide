# === Try / Except ===
try: # Code that may raise an exception
    result = 10 / 0  # This will raise a ZeroDivisionError
except ZeroDivisionError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

# === Try / Except / Else ===
# The else block runs only if no exception was raised
try:
    result = 10 / 2
except ZeroDivisionError as e:
    print(f"Error: {e}")
else:
    print(f"Result: {result}") # Output: Result: 5.0

# === Try / Except / Finally ===
# The finally block always runs, whether or not an exception occurred
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"Error: {e}") # Output: Error: division by zero
finally:
    print("Execution finished.") # Output: Execution finished.

# === Raise ===
# Manually triggering an exception
def check_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    return age

try:
    check_age(-5)
except ValueError as e:
    print(f"Error: {e}") # Output: Error: Age cannot be negative

# === Custom Exception ===
# Defining your own exception type by subclassing Exception
class InsufficientFundsError(Exception):
    pass

def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientFundsError(f"Cannot withdraw {amount}, balance is {balance}")
    return balance - amount

try:
    withdraw(100, 150)
except InsufficientFundsError as e:
    print(f"Error: {e}") # Output: Error: Cannot withdraw 150, balance is 100

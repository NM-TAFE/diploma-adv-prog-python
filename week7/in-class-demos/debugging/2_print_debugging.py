import time
import inspect
import logging
import pprint
import traceback

# Toggle for debug prints
debug = False

def log_message(message):
    """Prints a message with contextual information."""
    caller = inspect.stack()[1]
    pprint.pprint(caller) # test for the method sending the error

def conditional_print(message):
    """Prints a message only if debugging is enabled."""
    if debug:
        print(f"Conditional print: ${message}")

def process_numbers(numbers):
    """Processes a list of numbers by filtering and modifying them."""
    
    try:
        # Step 1: Filter out negative numbers
        filtered = [num for num in numbers if num >= 0]
        conditional_print(f"Filtered non-negative numbers: {filtered}")

        # Step 2: Multiply each remaining number by 2
        modified = [num * 2 for num in filtered]
        conditional_print(f"Modified numbers (doubled): {modified}")

        # Print detailed structure of modified numbers
        pprint.pp(modified)
        
        return modified
    except Exception as e:
        traceback.print_exc()
        return None

# Sample data to process
# numbers = [5, -3, 2, -8, 7, 10, -1, 0]
numbers = [5, -3, 'a', -8, 7, 10, -1, 0]

try:
    result = process_numbers(numbers)
    log_message(process_numbers(numbers))
except Exception as error:
    traceback.print_exc()
    traceback_string = traceback.format_exc()

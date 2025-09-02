import time
import inspect
import logging
import pprint
import traceback

# Set up logging
# logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Configuring logging to write to a file
# logging.basicConfig(filename='./logs/_app.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Logging levels
# logging.debug("This is a debug message")
# logging.info("This is an info message")
# logging.warning("This is a warning message")
# logging.error("This is an error message")
# logging.critical("This is a critical message")

# Toggle for debug prints
debug = True

def log_message(message):
    """Prints a message with contextual information."""
    caller = inspect.stack()[1]
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    pprint.pprint(caller) # test for the method sending the error
    # logging.info(f"Log Message output: [{timestamp}] {caller.function} (line {caller.lineno}): {message}")

def conditional_print(message):
    """Prints a message only if debugging is enabled."""
    if debug:
        print(f"Conditional print: ${message}")

def process_numbers(numbers):
    """Processes a list of numbers by filtering and modifying them."""
    # log_message(f"Received numbers: {numbers}")
    
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
        # logging.error(f"Error processing numbers: {e}")
        traceback.print_exc()
        return None

# Sample data to process
numbers = [5, -3, 2, -8, 7, 10, -1, 0]
# numbers = [5, -3, 'a', -8, 7, 10, -1, 0]

try:
    result = process_numbers(numbers)
    # log_message(f"Final result: {result}") # change to incorrect variable name
except Exception as error:
    # logging.error(f"An unexpected error occurred: {error}")
    traceback.print_exc()
    traceback_string = traceback.format_exc()
    # logging.error("Unhandled exception: %s\n%s", error, traceback_string)

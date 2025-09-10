import logging

# Setup basic config for logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Our decorator
def logger(func):
    # *args any number of positional arguments as a tuple
    # **kwargs any number of keyword arguments as a dictionary
    def wrapper(*args, **kwargs):
        print('Args: ',args)
        print('Kwargs: ',kwargs)
        # log the function
        logging.info(f"Running function: {func.__name__}")
        return func(*args, **kwargs)
    return wrapper


@logger
def greet(name, key, *args):
# def greet(name, key, **kwargs):
    print(f"Hi, {name}")

greet("Robbo", 'firstname', 'Stott', 'secondname')
# greet(name="Robbo", key="firstname", name2="Stott", key2="secondname")
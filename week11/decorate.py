from functools import wraps
from typing import Callable
def intro(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        """I am not the f function"""
        print("Welcome to the intro")
        func(*args, **kwargs)
    return wrapper

def conclusion(greeting: str) -> Callable:
    def custom_conclusion(func: Callable) -> Callable:
        def wrapper(*args, **kwargs):
            func(*args, **kwargs)
            print(f"{greeting} from conclusion")
        return wrapper
    return custom_conclusion
@intro
def f(name):
    """I am the f function"""
    print(f"Hello {name}")



@conclusion("Inception")
@intro
def g():
    print("Hello from g")




# g = intro(g)
# f = intro(f)
g()


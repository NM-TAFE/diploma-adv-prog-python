from functools import wraps, partial
import time


def retry_decorator(func=None, *, tries=1, wait=1):
    if func is None:
        # If func is None, the decorator has been called with arguments.
        # Return a partial object that will be called again with the function to decorate.
        return partial(retry_decorator, tries=tries, wait=wait)

    @wraps(func)
    def wrapper(*args, **kwargs):
        # nonlocal tries
        for _ in range(tries):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                print(f'Error: {e}, retrying in {wait} seconds...')
                time.sleep(wait)
        return func(*args, **kwargs)

    return wrapper


# The decorator can be used without parentheses:
@retry_decorator
def test_retry_no_args():
    print('Testing retry without args')
    raise ValueError('Failed without args')


# Or with parentheses, including arguments:
@retry_decorator(tries=3, wait=2)
def test_retry_with_args():
    print('Testing retry with args')
    raise ValueError('Failed with args')


# To demonstrate, you'll need to call these functions:
try:
    test_retry_no_args()
except ValueError:
    pass

try:
    test_retry_with_args()
except ValueError:
    pass

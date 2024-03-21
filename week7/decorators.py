from functools import partial, wraps
def outer_decorator(func=None, repeat = 3):
    if func is None:
        return partial(outer_decorator, repeat=repeat)

    @wraps(func)
    def wrapped(*args, **kwargs):
        for _ in range(repeat):
            print("do something wrapped")
        return func(*args, **kwargs)
    return wrapped


@outer_decorator
def hello():
    print("Hello")
hello()
print(hello)
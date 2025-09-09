# def d(countdown):
#     if countdown <= 1:
#         return 1
#     print(countdown)
#     return d(countdown - 1)

def c():
    my_var = 3
    return 42
def b():
    my_var = 2
    return c() + my_var

def a():
    my_var = 1
    return b() + my_var


# TODO: write a version of this that returns a list with countdown values


def countdown_list(n: int) -> list[int]:
    """returns a countdown as a list such that:
    [n, n - 1, n -2, ..., 1]
    """
def countdown(value):
    if value < 1:
        return 0
    print(value)
    countdown(value - 1)
    return None

countdown(5)
# [5, 4, 3, 2, 1]
# print(a())

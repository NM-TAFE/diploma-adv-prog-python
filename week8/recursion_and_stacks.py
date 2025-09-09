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
def countdown(value):
    if value < 1:
        return 0
    print(value)
    countdown(value - 1)
    return None

countdown(1000)
# print(a())

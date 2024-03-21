def c(v):
    return v + 1
def b(v):
    return c(v) + 1
def a(v, runs):
    return b(v) + 1

def a(v, runs):
    if runs <= 0:
        return v + 1
    runs -= 1
    return a(v, runs) + 1

print(a(4, runs=2))
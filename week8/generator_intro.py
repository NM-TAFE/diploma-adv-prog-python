def hello():
    print("before 42")
    yield 42
    print("before 43")
    yield 43
    print("before 44")
    yield from (i for i in range(10))
    print("end")

for x in hello():
    print(x)
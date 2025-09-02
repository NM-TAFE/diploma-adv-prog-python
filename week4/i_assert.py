def add_two(a):
    if a % 2 == 0:
        return a + 2
    return a + 2
def test():
    # print("I assert that 4 -> 6", add_two(4))
    assert add_two(4) == 6, "should add two"
    assert add_two(5) == 5
if __name__ == '__main__':
    test()
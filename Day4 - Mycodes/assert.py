def square(x):
    return x * x
def test_square():
    assert square(2) == 4
    assert square(-3) == 10
    assert square(0) == 0
    print("All unit tests passed!")

test_square()
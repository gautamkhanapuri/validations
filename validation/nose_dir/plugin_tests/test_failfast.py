from nose2.tools import params

@params("Sir Bedevere", "Miss Islington", "Duck")
def test_is_knight(value):
    assert value.startswith('Sir')

def test_example():
    assert 1 + 1 == 1

def test_addition():
    assert 1 + 1 == 2

def test_subtraction():
    assert 2 - 1 == 2

def test_multiplication():
    assert 2 * 2 == 3

def test_division():
    assert 4 / 2 == 2

def test_complex_calculation():
    result = (2 + 2) * (2 - 1) / 2
    assert result == 2, "Expected 2, but got %d" % result


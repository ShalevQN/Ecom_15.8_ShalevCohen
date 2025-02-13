import pytest
import calculator

def test_power_a():
    # arrange
    a: int = 2
    b: int = 4
    expected: int = 16
    # act
    actual: int = calculator.power(a, b)
    #assert
    assert expected == actual, "test power func (2, 4)"


def test_power_b():
    # arrange
    a: int = 3
    b: int = 2
    expected: int = 9
    # act
    actual: int = calculator.power(a, b)
    #assert
    assert expected == actual, "test power func (3, 2)"

def test_sqrt_a():
    # arrange
    a: int = 25
    expected: int = 5
    # act
    actual: int = calculator.sqrt(a)
    #assert
    assert expected == actual, "test power sqrt (25)"

def test_sqrt_b():
    # arrange
    a: int = -5
    expected: int = 0
    # act
    actual: int = calculator.sqrt(a)
    #assert
    assert expected == actual, "test power sqrt (-5)"

def test_check_error_happened():
    with pytest.raises(ValueError) as ex:
        calculator.make_value_error(ex)


def test_factorial_a():
    # arrange
    a: int = 4
    expected: int = 24
    # act
    actual: int = calculator.factorial(a)
    #assert
    assert expected == actual, "test power factorial (4)"

def test_factorial_b():
    # arrange
    a: int = 5
    expected: int = 120
    # act
    actual: int = calculator.factorial(a)
    #assert
    assert expected == actual, "test power factorial (5)"

def test_factorial_c():
    # arrange
    a: int = -3
    expected: int = 0
    # act
    actual: int = calculator.factorial(a)
    #assert
    assert expected == actual, "test power factorial (-3)"

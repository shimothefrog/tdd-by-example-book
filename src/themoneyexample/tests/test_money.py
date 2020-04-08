import pytest

from src.themoneyexample.dollar import Dollar


class TestMoney:
    def test_multiplication(self):
        five = Dollar(5)
        product: Dollar = five.times(2)
        assert 10 == product.amount
        product: Dollar = five.times(3)
        assert 15 == product.amount

    def test_equality(self):
        assert True is Dollar(5).equals(Dollar(5))
        assert False is Dollar(5).equals(Dollar(6))

import pytest

from src.themoneyexample.dollar import Dollar


class TestMoney:
    def test_multiplication(self):
        five = Dollar(5)
        five.times(2)
        assert 10 == five.amount

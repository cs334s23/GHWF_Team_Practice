import pytest
from double_number import double_number

def test_double_number():
    assert double_number(3) == 6
    assert double_number(10) == 20
    assert double_number(0) == 0
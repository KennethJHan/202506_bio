import pytest
from p_1330 import comp


@pytest.mark.parametrize(
    ("num1, num2, expected"), [(1, 2, "<"), (5, 2, ">"), (10, 10, "==")]
)
def test_comp(num1, num2, expected):
    assert comp(num1, num2) == expected

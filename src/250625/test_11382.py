import pytest
from p_11382 import add3


@pytest.mark.parametrize(
    ("n1, n2, n3, expected"),
    [
        (77, 77, 7777, 7931),
        (10, 20, 30, 60),
    ],
)
def test_add3(n1, n2, n3, expected):
    assert add3(n1, n2, n3) == expected

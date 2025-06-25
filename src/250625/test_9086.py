import pytest
from p_9086 import get_first_last_char


@pytest.mark.parametrize(
    ("instr, expected"), [("ABCD", "AD"), ("O", "OO"), ("AB", "AB")]
)
def test_get_first_last_char(instr, expected):
    assert get_first_last_char(instr) == expected

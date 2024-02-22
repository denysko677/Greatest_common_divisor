import pytest
from your_module import gcd

@pytest.mark.parametrize("a, b, expected_gcd", [
    (10, 25, 5),
    (14, 28, 14),
    (21, 49, 7),
    (30, 18, 6),
    (17, 23, 1),
])
def test_gcd(a, b, expected_gcd):
    assert gcd(a, b) == expected_gcd

def test_gcd_with_zero():
    assert gcd(0, 5) == 5
    assert gcd(5, 0) == 5
    assert gcd(0, 0) == 0

def test_gcd_negative_numbers():
    assert gcd(-10, 25) == 5
    assert gcd(10, -25) == 5
    assert gcd(-10, -25) == 5
    assert gcd(-21, -49) == 7

if __name__ == "__main__":
    pytest.main()

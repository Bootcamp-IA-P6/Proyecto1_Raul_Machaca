from taximeter import calculate_fare

def test_calculate_fare_basic():
    result = calculate_fare(10, 10)
    expected = (10 * 0.02) + (10 * 0.05)
    assert result == expected


def test_calculate_fare_zero():
    result = calculate_fare(0, 0)
    assert result == 0

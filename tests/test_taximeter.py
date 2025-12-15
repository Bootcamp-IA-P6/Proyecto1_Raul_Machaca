from taximeter import Trip

def test_calculate_fare_basic():
    trip = Trip()
    trip.stopped_time = 10
    trip.moving_time = 10
    assert trip.calculate_fare() == 10*0.02 + 10*0.05

def test_calculate_fare_zero():
    trip = Trip()
    trip.stopped_time = 0
    trip.moving_time = 0
    assert trip.calculate_fare() == 0

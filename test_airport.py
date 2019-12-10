import pytest
from class_passenger import *
from class_plane import *
from class_flight_trip import *

# class Pass_test():
def test_passenger():
    assert Passenger('Joana Thomson', 'B343123').name == 'Joana Thomson'
    assert Passenger('Birt Kuman', 'B13927').passport_num == 'B13927'

def test_Flight():
    new_trip = Flight_Trip()
    assert isinstance(new_trip,Flight_Trip)

def test_plane():
    plane1 = Plane('123')
    assert isinstance(plane1, Plane)

def test_flight_plane():
    new_trip = Flight_Trip()
    new_trip.add_plane('BA222')
    assert new_trip.plane == 'BA222'

def test_flight_destination():
    new_trip = Flight_Trip()
    new_trip.add_destination('London')
    assert new_trip.destination == ('London')

def test_flight_origin():
    new_trip = Flight_Trip()
    new_trip.add_origin('LA')
    assert new_trip.origin == ('LA')

def test_list_of_passengers():
    new_trip = Flight_Trip()
    new_trip.add_passenger('Jerome')
    assert new_trip.passengers[0] == ('Jerome')
    assert type(new_trip.passengers) == type([])

def test_missing_info():
    with pytest.raises(TypeError):
        Passenger()
    with pytest.raises(TypeError):
        Passenger('Joana')
    with pytest.raises(TypeError):
        Passenger('123')
    with pytest.raises(TypeError):
        Plane()


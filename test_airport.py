from class_passenger import *
from class_plane import *
from class_flight_trip import *

# class Pass_test():
def test_passenger():
    assert Passenger('Joana Thomson', 'B343123').name == 'Joana Thomson'
    assert Passenger('Birt Kuman', 'B13927').passport_num == 'B13927'


# def test_passenger_error(name, passport_num):
#     assert Passenger('Joana Thomson').name == 'Please make sure both the arguments have been inputted'

def test_plane():
    assert Plane('222').plane_num == '222'

def test_flight_plane():
    new_trip = Flight_Trip()
    new_trip.add_plane('BA222')
    assert new_trip.plane == 'BA222'

def test_flight_destination():
    new_trip = Flight_Trip()
    new_trip.add_destination('London')
    assert new_trip.destination == ('London')
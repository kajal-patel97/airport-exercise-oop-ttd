import class_flight_trip
import class_passenger
from class_passenger import *

from class_plane import *

from class_flight_trip import *

flight1 = class_flight_trip.Flight_Trip('BA79845', 'LA', 'London')
flight2 = class_flight_trip.Flight_Trip('BA48964', 'Morocco', 'Canada')
flight3 = class_flight_trip.Flight_Trip('BA15264', 'Las Vegas', 'Toronto')
flight4 = class_flight_trip.Flight_Trip('BA78884', 'Bali', 'Dubai')
flight_list = []
flight_list.extend([flight1, flight2, flight3, flight4])

while True:
    print('Please select from the following...')
    print('1 -- Create a Passenger')
    print('2 -- Add a passenger to a Flight ')
    print('3 -- List all Flights ')

    option = input('Please select a number from the options listed...')

    if option == '1':
        print('You have selected option 1 - Create a Passenger')
        name = input('What is the name of the passenger you would like to create?')
        pass_num = input('What is their passport number?')
        passenger_created = class_passenger.Passenger(name, pass_num)
        print(f'Well done you have added, Name: {name.title()}, with the Passport Number:{pass_num}')

    elif option == '2':
        print('You have selected option 2 - Add passenger to Flight')
        passenger = input('What passenger would you like to add to the flight? ')
        add_passenger_to_flight = flight1.add_passenger(passenger)
        print(f'You have added {passenger} to {flight1.plane}')

    elif option == '3':
        print('You have selected option 3 - List all Flights')
        for flights in flight_list:
            print(flights.plane)

    else:
        break

import pyodbc
from connect_sql import *
from class_passenger import *
from class_plane import *
from class_flight_trip import *


while True:
    print('Please select from the following...')
    print('1 -- Create a Passenger')
    print('2 -- Add a passenger to a Flight ')
    print('3 -- List all Flights ')

    option = input('Please select a number from the options listed...')

    if option == '1':
        print('You have selected option 1 - Create a Passenger')
        create_passenger = Passenger.create_passenger()
        print(create_passenger)
        print('You have Created a Passenger')


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

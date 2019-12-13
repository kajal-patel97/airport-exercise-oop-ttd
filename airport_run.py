import pyodbc
from connect_sql import *
from class_passenger import *
from class_plane import *
from class_flight_trip import *
table_passenger = Passenger()
table_flight = Flight_Trip

while True:
    print('Please select from the following...')
    print('1 -- Create a Passenger')
    print('2 -- Add a passenger to a Flight ')
    print('3 -- List all Flights ')

    option = input('Please select a number from the options listed...')

    if option == '1':
        print('You have selected option 1 - Create a Passenger')
        table_passenger.create_passenger()
        print('You have Created a Passenger')


    elif option == '2':
        print('You have selected option 2 - Add passenger to Flight')
        table_passenger.add_passenger_to_flight()
        print('You Have added a passenger to a flight ')

    elif option == '3':
        print('You have selected option 3 - List all Flights')
        for flights in flight_list:
            print(flights.plane)

    else:
        break

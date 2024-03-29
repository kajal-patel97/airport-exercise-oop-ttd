import pyodbc
from connect_sql import *
from class_passenger import *
from class_plane import *
from class_flight_trip import *

table_passenger = Passenger()
table_flight = Flight_Trip()
table_plane = Plane()

while True:
    print('Please select from the following...')
    print('____________________________________________')
    print('1 -- Create a Passenger')
    print('2 -- Search for Passenger')
    print('3 -- Create a Flight')
    print('4 -- List all Flights ')
    print('5 -- Add a passenger to a Flight ')

    print('6 -- Add a Plane')
    print('7 -- List all Planes')
    print('____________________________________________')

    option = input("Please select a number from the options listed...('exit' to quit)")

    if option == '1':
        print('You have selected option 1 - Create a Passenger')
        table_passenger.create_passenger()
        print('You have Created a Passenger')

    elif option == '2':
        print('You have selected option 2 - Search for a Passenger ')
        table_passenger.search_passenger()
        print(('Here are all the passengers'))

    elif option == '3':
        print('You have selected option 3 - Create a Flight')
        table_flight.create_flight()
        print('You have created a flight!')


    elif option == '4':
        print('You have selected option 4 - List all Flights')
        table_flight.list_flights()
        print('Completed')

    elif option == '5':
        print('You have selected option 2 - Add passenger to Flight')
        table_passenger.add_passenger_to_flight()
        print('You have added a passenger to a flight ')


    elif option == '6':
        print('You have selected option 6 - Add a Plane')
        table_plane.add_plane()
        print('You have added a plane!')

    elif option == '7':
        print('You have chosen to list all the planes available')
        plane = table_plane.get_all_planes()
        print(plane)


    else:
        break

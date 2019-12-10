from class_passenger import *
from class_plane import *
from class_flight_trip import *

while True:
    print('Please select from the following...')
    print('1 -- Create a Passenger')
    print('2 -- Create a New Flight')
    print('3 -- Add a passenger to a Flight ')
    print('4 -- List all passengers in Flight')
    print('5 -- List all Flights ')

    option = input('Please select a number from the options listed...')

    if option == '1':
        print('You have selected option 1 - Create a Passenger')
        name = input('What is the name of the passenger you would like to create?')
        pass_num = input('What is their passport number?')
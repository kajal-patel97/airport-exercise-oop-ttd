from class_passenger import *
name = input('What is the name you want to add?  ')
passport_num = input('What is their passport number?   ')
passenger1 = Passenger(name, passport_num)


# as a user I can create a Passenger
print('checking to see if i can create a passenger')
print(passenger1.create_passenger(name, passport_num) == 'You have added Joana Thomson with the passport number : B343123')
print("got:", passenger1.create_passenger('Joana Thomson', 'B343123'))
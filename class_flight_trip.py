# - As a user I can create a flight with no specific information
# - as a user I can add a plane
# - as a User I can add a destination
# - As a user I can add a origin
# - As a user I can add a Passanger to the list of passangers
# - Passanger list is a list of objct that are Passanger

class Flight_Trip():
    def __init__(self):
        self.plane = ''
        self.destination = ''
        self.origin = ''
        self.passengers = []

    def add_plane(self, plane_num):
        self.plane = plane_num

    def add_destination(self, destination_name):
        self.destination = destination_name

    def add_origin(self,origin_name):
        self.origin = origin_name

    def add_passenger(self, passenger):
        self.passengers.append(passenger)
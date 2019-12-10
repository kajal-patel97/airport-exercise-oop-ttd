class Passenger():

    def __init__(self, name, passport_num):
        self.name = name
        self.passport_num = passport_num


    def create_passenger(self, name, passport_num):
        return f'You have added {name} with the passport number : {passport_num}'

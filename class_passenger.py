class Passenger():

    def __init__(self, name, passport_num):
        self.name = name
        self.passport_num = passport_num
        try:
            Passenger()
        except TypeError as error:
            print('Have you passed through the passengers name and passport number?')





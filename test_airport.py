from class_passenger import *

# class Pass_test():
def test_passenger():
    assert Passenger('Joana Thomson', 'B343123').name == 'Joana Thomson'
    assert Passenger('Birt Kuman', 'B13927').passport_num == 'B13927'



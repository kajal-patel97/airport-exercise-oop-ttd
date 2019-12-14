import pyodbc
from connect_sql import *

class Passenger(MSDBConnection):

    #Create a passenger and insert it into the database
    def create_passenger(self):
        first_name = input('What is the passengers first name?')
        last_name = input('What is their last name?')
        passport_number = input('What is their passport number?  ')
        query = f"INSERT INTO passengers (first_name, last_name, passport_number) VALUES ('{first_name}', '{last_name}', '{passport_number}')"
        result = self._MSDBConnection__sql_query(query)
        self.docker_airport_python.commit()
        return result


    def add_passenger_to_flight(self):
        ask_flight = input('What is the flight ID you would like to add the passenger to?..')
        passport_number = input('What is the passport number of the passenger you would like to add to this flight?')
        query = f"UPDATE passengers SET flight_id = '{ask_flight}' WHERE passport_number ='{passport_number}' "
        result = self._MSDBConnection__sql_query(query)
        self.docker_airport_python.commit()
        return result

    def search_passenger(self):
        ask_passenger = input ('What is the name of your passenger? ')
        query = f"SELECT * FROM Passengers WHERE first_name LIKE '%{ask_passenger}%' OR last_name LIKE '%{ask_passenger}%' "
        result = self._MSDBConnection__sql_query(query)
        print('Here is what we found...')
        while True:
            record = result.fetchone()
            if record is None:
                break
            print(record)
        return 'All results completed'

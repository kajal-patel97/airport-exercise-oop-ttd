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
        ask_name = input('What is the full name of the passenger you would like to add to this flight?')
        query = f"INSERT INTO passengers (flight_id) VALUES ('{ask_flight}') WHERE first_name LIKE '%{ask_name}%' OR last_name LIKE '%{ask_name}%'"
        result = self._MSDBConnection__sql_query(query)
        self.docker_airport_python.commit()
        return result



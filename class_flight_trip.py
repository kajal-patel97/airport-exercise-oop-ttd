from connect_sql import *
import pyodbc

class Flight_Trip(MSDBConnection):

    def create_flight(self):
        ask_plane = input('What is the ID of the plane you would like to add? ')
        ask_orgin = input('Where is the flight departing from?')
        ask_destination = input('Where is the flight going to ? ')
        query = f"INSERT INTO Flight_Trip (plane_id, origin, destination) VALUES ('{ask_plane}','{ask_orgin}','{ask_destination}')"
        result = self._MSDBConnection__sql_query(query)
        self.docker_airport_python.commit()
        return result

    def list_flights(self):
        print('Listing all the flights we have available...')
        query  = "SELECT * FROM Flight_trip"
        result = self._MSDBConnection__sql_query(query)
        print('This is what we found....')
        while True:
            record = result.fetchone()
            if record is None:
                break
            print(record)


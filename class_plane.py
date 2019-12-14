
import pyodbc
from connect_sql import *
#As a User I can create a Plane with a plane number

class Plane(MSDBConnection):

  def add_plane(self):
    ask_plane = input('What is the plane number? ')
    query = f"INSERT INTO Plane (plane_number) VALUES ('{ask_plane}')"
    result = self._MSDBConnection__sql_query(query)
    self.docker_airport_python.commit()
    return result

  def get_all_planes(self):
    query = "SELECT * FROM Plane"
    result = self._MSDBConnection__sql_query(query)
    print("Here are a list of all the planes ")
    while True:
        record = result.fetchone()
        if record is None:
            break
        print(record)
    return 'Completed'

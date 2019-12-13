import pyodbc

class MSDBConnection():

    def __init__(self):
        self.server = 'localhost, 1433'
        self.database = 'airport_python'
        self.user_name = 'SA'
        self.password = 'Passw0rd2018'


        #Making the connection

        self.docker_airport_python = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+user_name+';PWD='+ password)

        #Making a cursor
        self.cursor = self.docker_airport_python.cursor() # creates an object which is a cursor

        #method for sql query
    def __sql_query(self, sql_query):
        return self.cursor.execute(sql_query)




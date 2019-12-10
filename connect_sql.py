import pyodbc

#These are our variables we have to connect
server = 'localhost, 1433'
database = 'airport_python'
user_name = 'SA'
password = 'Passw0rd2018'

#Making the connection

docker_airport_python = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+user_name+';PWD='+ password)

#Making a cursor
cursor = docker_airport_python.cursor() # creates an object which is a cursor

cursor.execute("SELECT * FROM passengers")
row = cursor.fetchone()
print(row)


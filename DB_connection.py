import mysql.connector

db_connection = mysql.connector.connect(user='root',
							  			password='3935GrayFuse',
							  			host='localhost',
										database='flight_hours_db')

my_cursor = db_connection.cursor()

my_cursor.execute("INSERT into crew_members values (11111111, 'Nick', 'Westbrooks', 'SonicNess', 'SO');")

#Replace '*****' with SQL command in function you use it in'''



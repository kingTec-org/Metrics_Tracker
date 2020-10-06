import mysql.connector

db_connection = mysql.connector.connect(user='root',
							  			password='3935GrayFuse',
							  			host='localhost',
										database='flight_hours_db')
my_cursor = db_connection.cursor()




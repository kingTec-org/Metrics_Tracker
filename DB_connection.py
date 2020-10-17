import mysql.connector

conn = mysql.connector.connect(user='root',
							   password='3935GrayFuse',
							   host='localhost',
							   database='flight_hours_db')

my_cursor = conn.cursor(buffered=True)

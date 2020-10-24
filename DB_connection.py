import mysql.connector
from PyQt5 import QtSql, QtCore

#print(QtCore.QCoreApplication.libraryPaths())
# QT MYSQL CONNECTOR, NEED DRIVER,
#TODO FIGURE OUT THE DRIVER ISSUE
#db = QtSql.QSqlDatabase.addDatabase("QMYSQL")
#db.setHostName("localhost")
#db.setDatabaseName("flight_hours_db")
#db.setUserName("root")
#db.setPassword("3935GrayFuse")
#query = QtSql.QSqlQuery()

conn = mysql.connector.connect(user='root',
							   password='3935GrayFuse',
							   host='localhost',
							   database='flight_hours_db')

my_cursor = conn.cursor(buffered=True)

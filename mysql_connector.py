import mysql.connector


# get crew member list from database
def get_crew_query():
	conn = mysql.connector.connect(
		user='root',
		password='3935GrayFuse',
		host='localhost',
		database='flight_hours_db'
	)

	curs = conn.cursor(buffered=True)

	print('Connected to Database')

	curs.execute('SELECT * FROM crew_members')

	get_crew = curs.fetchall()

	crew_member_list = []

	for crew in get_crew:
		employee_id_number = str(crew[0])
		last_name = str(crew[1])
		first_name = str(crew[2])
		middle_name = str(crew[3])
		crew_position = str(crew[4])
		crew_member_list.append(
			[[f'{employee_id_number}'],
			 [f'{last_name}'],
			 [f'{first_name}'],
			 [f'{middle_name}'],
			 [f'{crew_position}']])

		curs.close()
		conn.close()

	return crew_member_list


# get column_names from database
def get_column_names():
	conn = mysql.connector.connect(
		user='root',
		password='3935GrayFuse',
		host='localhost',
		database='flight_hours_db'
	)

	curs = conn.cursor(buffered=True)

	print('Connected to Database')

	curs.execute(
		'''
		SHOW columns FROM crew_members;
		'''
	)
	get_column_names = curs.fetchall()

	column_name_list = []

	for column in get_column_names:
		header = {column}
		column_name_list.append(header)

	curs.close()
	conn.close()

	return column_name_list


print(get_column_names()[0])

import DB_connection


class Crewmember:
	'''This class is used to add a new Crewmember to the datebase'''

	def __init__(self, employee_number, first_name, last_name, middle_name, crew_position):
		self.employee_number = employee_number
		self.first_name = first_name
		self.last_name = last_name
		self.middle_name = middle_name
		self.crew_position = crew_position
		self.full_name = f"{last_name}, {first_name} {middle_name}"


def add_crew_member(employee_number, last_name, first_name, middle_name, crew_position):
	add_new_crew = f"INSERT into crew_members values ('{employee_number}', '{last_name}', '{first_name}', " \
				   f"'{middle_name}', '{crew_position}');"
	DB_connection.my_cursor.execute(add_new_crew)
	DB_connection.db_connection.commit()
	print('done')

#add_crew_member(11111113, 'Westbrooks', 'Nick', 'NULL', 'SO')

#example of how to use function: add_crew_member(11111112, 'Nick', 'Stewart', 'Crishaun', 'SO')

#my_cursor.execute("INSERT into crew_members values (11111111, 'Nick', 'Westbrooks', 'SonicNess', 'SO');")





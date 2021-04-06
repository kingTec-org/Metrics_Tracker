import mysql.connector
import names
import random


# generates fake crew members on the table for testing
def add_fake_crew_members(num):
	conn = mysql.connector.connect(
		user='root',
		password='3935GrayFuse',
		host='localhost',
		database='metrics_db'
	)

	curs = conn.cursor(buffered=True)

	print('Connected to Database')

	crew_pos_list = ['P', 'SO', 'IP', 'ISO', 'EP', 'ESO']

	i = 1
	for x in range(num):
		try:
			employee_number = random.randint(13370000, 13380000)
			first_name = names.get_first_name()
			first_name = ''.join(("'", first_name, "'"))
			last_name = names.get_last_name()
			last_name = ''.join(("'", last_name, "'"))
			middle_name = names.get_first_name()
			middle_name = ''.join(("'", middle_name, "'"))
			crew_position = random.choice(crew_pos_list)
			crew_position = ''.join(("'", crew_position, "'"))
			query = f'INSERT INTO crew_members (employee_number, last_name, first_name, middle_name, crew_position) ' \
					f'VALUES ({employee_number}, {last_name}, {first_name}, {middle_name}, {crew_position});'

			curs.execute(query)
			conn.commit()

		except:
			print(f'{i}. Fix Your Query')
			i += 1
			pass

	curs.close()
	conn.close()

	print('Disconnected from Database')


def add_fake_sites(num):
	conn = mysql.connector.connect(
		user='root',
		password='3935GrayFuse',
		host='localhost',
		database='metrics_db'
	)

	curs = conn.cursor(buffered=True)

	print('Connected to Database')

	country_list = ['United States', 'Limnadia', 'Tatoooine', 'Hogwarts', 'Middle Earth', 'Westeros']

	i = 1
	for x in range(num):
		try:
			site_id = random.randint(11, 99)
			country = random.choice(country_list)
			country = ''.join(("'", country, "'"))
			num_ac = random.randint(1, 5)
			num_full_staff = num_ac * 10
			num_curr_staff = random.randint(num_full_staff - random.randint(1, 6), num_full_staff)
			query = f'INSERT INTO sites (site_id, country, num_ac, num_full_staff, num_curr_staff) ' \
					f'VALUES ({site_id}, {country}, {num_ac}, {num_full_staff}, {num_curr_staff});'

			curs.execute(query)
			conn.commit()

		except:
			print(f'{i}. Fix Your Query')
			i += 1
			pass

	curs.close()
	conn.close()

	print('Disconnected from Database')

	return None


# get crew member list from database
def get_crew_query():
	conn = mysql.connector.connect(
		user='root',
		password='3935GrayFuse',
		host='localhost',
		database='metrics_db'
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

	print('Disconnected from Database')

	return crew_member_list


# get site list from database
def get_site_query():
	conn = mysql.connector.connect(
		user='root',
		password='3935GrayFuse',
		host='localhost',
		database='metrics_db'
	)

	curs = conn.cursor(buffered=True)

	print('Connected to Database')

	curs.execute('SELECT * FROM sites')

	get_site = curs.fetchall()

	site_list = []

	for site in get_site:
		site_id = str(site[0])
		country = str(site[1])
		num_ac = str(site[2])
		num_full_staff = str(site[3])
		num_curr_staff = str(site[4])
		site_list.append(
			[[f'{site_id}'],
			 [f'{country}'],
			 [f'{num_ac}'],
			 [f'{num_full_staff}'],
			 [f'{num_curr_staff}']])

		curs.close()
		conn.close()

	print('Disconnected from Database')

	return site_list


# get column_names from database
def get_crew_column_query():
	conn = mysql.connector.connect(
		user='root',
		password='3935GrayFuse',
		host='localhost',
		database='metrics_db'
	)

	curs = conn.cursor(buffered=True)

	print('Connected to Database')

	curs.execute(
		'''
		SHOW columns FROM crew_members;
		'''
	)
	get_column_names = curs.fetchall()

	crew_column_name_list = []

	for column in get_column_names:
		column_name = f'{column[0].replace("_", " ").title()}'
		crew_column_name_list.append(column_name)

	curs.close()
	conn.close()

	print('Disconnected from Database')

	return crew_column_name_list


def get_site_column_query():
	conn = mysql.connector.connect(
		user='root',
		password='3935GrayFuse',
		host='localhost',
		database='metrics_db'
	)

	curs = conn.cursor(buffered=True)

	print('Connected to Database')

	curs.execute(
		'''
		SHOW columns FROM sites;
		'''
	)
	get_column_names = curs.fetchall()

	site_column_name_list = []

	for column in get_column_names:
		column_name = f'{column[0].replace("_", " ").title()}'
		site_column_name_list.append(column_name)

	curs.close()
	conn.close()

	print('Disconnected from Database')

	return site_column_name_list

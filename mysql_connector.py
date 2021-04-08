import mysql.connector
import names
import random


# generates fake crew members on the table for testing
def add_fake_crew_members(num):
	def raw_get_crew_column_query():
		conn = mysql.connector.connect(
			user='root',
			password='3935GrayFuse',
			host='localhost',
			database='metrics_db'
		)

		curs = conn.cursor(buffered=True)

		curs.execute(
			'''
			SHOW columns FROM crew_members;
			'''
		)
		get_column_names = curs.fetchall()

		raw_crew_column_name_list = []

		for column in get_column_names:
			column_name = column[0]
			raw_crew_column_name_list.append(column_name)

		raw_crew_column_name_list = (', '.join(raw_crew_column_name_list))

		curs.close()
		conn.close()

		return raw_crew_column_name_list

	conn = mysql.connector.connect(
		user='root',
		password='3935GrayFuse',
		host='localhost',
		database='metrics_db'
	)

	curs = conn.cursor(buffered=True)

	crew_pos_list = ['P', 'SO', 'IP', 'ISO', 'EP', 'ESO']

	i = 1
	for x in range(num):
		# try:
		employee_number = random.randint(13370000, 13380000)

		first_name = names.get_first_name()

		last_name = names.get_last_name()

		middle_name = names.get_first_name()

		crew_position = random.choice(crew_pos_list)

		new_crew = (int(f'{employee_number}'), f'{last_name}', f'{first_name}', f'{middle_name}',
					f'{crew_position}')

		column_list = raw_get_crew_column_query()

		query = f'INSERT INTO crew_members ({column_list}) VALUES (%s, %s, %s, %s, %s);'

		try:
			print(query, new_crew)
			curs.execute(query, new_crew)
			conn.commit()

		except:
			conn.rollback()
			print(f'{i}. Fix Your Query')
			i += 1
			pass

	curs.close()
	conn.close()


# generates fake sites, just enter how many
def add_fake_sites(num):
	conn = mysql.connector.connect(
		user='root',
		password='3935GrayFuse',
		host='localhost',
		database='metrics_db'
	)

	curs = conn.cursor(buffered=True)

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

	curs.execute('SELECT * FROM crew_members')

	get_crew = curs.fetchall()

	crew_member_list = []

	def raw_get_crew_column_query():
		conn = mysql.connector.connect(
			user='root',
			password='3935GrayFuse',
			host='localhost',
			database='metrics_db'
		)

		curs = conn.cursor(buffered=True)

		curs.execute(
			'''
			SHOW columns FROM crew_members;
			'''
		)
		get_column_names = curs.fetchall()

		raw_crew_column_name_list = []

		for column in get_column_names:
			column_name = column[0]
			raw_crew_column_name_list.append(column_name)

		curs.close()
		conn.close()

		return raw_crew_column_name_list

	for column, crew in raw_get_crew_column_query(), get_crew:
		print(column, crew)


	for crew in get_crew:
		employee_id_number = str(crew[0])
		last_name = str(crew[1])
		suffix = str(crew[2])
		first_name = str(crew[3])
		middle_name = str(crew[4])
		crew_position = str(crew[5])
		crew_member_list.append(
			[[f'{employee_id_number}'],
			 [f'{last_name}'],
			 [f'{suffix}'],
			 [f'{first_name}'],
			 [f'{middle_name}'],
			 [f'{crew_position}']])

		curs.close()
		conn.close()

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

	return site_column_name_list

from pymongo import MongoClient
from pprint import pprint
import names
import random
import urllib.parse
import re

me = urllib.parse.quote_plus('LarryDCJ')
rd = urllib.parse.quote_plus('dismyside42')

client = MongoClient("mongodb+srv://%s:%s@cluster0.nhqsm.mongodb.net/metrics_tracker?retryWrites"
                     "=true&w=majority" % (me, rd), authSource='admin')

db = client['metrics_tracker']
crew_members = db['crew_members']


# get crew member list from database
def get_crew_query():
    crew_list = []
    for crew in crew_members.find():
        crew = crew.values()
        crew = list(crew)[1:]
        crew_list.append(crew)
    return crew_list


#
def get_crew_column_query():
    column_list = []
    for col in crew_members.find():
        col = list(col.keys())[1:]
        for column_header in col:
            column_list.append(column_header.title().replace('_', ' '))
        break
    return column_list

#
def get_site_query():
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
    return site_list


#
def find_all_via_crew_pos():
    result = db.crew_members.find({'crew_position': 'SO'})
    return result


#
def add_crew_members(start=1, end=151):
    def employee_number():
        em_id = random.randint(13370000, 13380000)
        return em_id

    suffix = ['Jr.', 'Sr.', 'III', 'IV', '', '', '', '', '', '', '', '', '', '', '']

    crew_pos_list = ['P', 'SO', 'IP', 'ISO', 'EP', 'ESO']

    gender = ['male', 'female']

    for x in range(start, end):
        gender = random.choice(gender)
        total = end - start
        crew_member = {
            'employee_id': employee_number(),
            'last_name': names.get_last_name(),
            'suffix': random.choice(suffix),
            'first_name': names.get_first_name(gender=gender),
            'middle_name': names.get_first_name(gender=gender),
            'crew_position': random.choice(crew_pos_list),
        }

        # Step 3: Insert business object directly into MongoDB via insert_one
        result = coll.insert_one(crew_member)

        # Step 4: Print to the console the ObjectID of the new document
        print(f'Created {x} of {total} as {result.inserted_id}')

    print('Done.')


# generates fake sites, just enter how many
def add_fake_sites(num):
    country_list = ['United States', 'Limnadia', 'Tatoooine', 'Hogwarts', 'Middle Earth', 'Westeros']


# get site list from database

